import os
import tensorstore as ts
import pandas as pd
import numpy as np
import scipy
import pickle
from anndata import AnnData
from typing import List, Union, Tuple
# import multiscale_spatial_image
import tqdm
from abc import ABC, ABCMeta
from enum import Enum, EnumMeta, unique
from functools import wraps
from typing import Any, Callable


class PrettyEnum(Enum):
    """Enum with a pretty :meth:`__str__` and :meth:`__repr__`."""

    @property
    def v(self) -> Any:
        """Alias for :attr`value`."""
        return self.value

    def __repr__(self) -> str:
        return f"{self.value!r}"

    def __str__(self) -> str:
        return f"{self.value!s}"

class ModeEnum(str, PrettyEnum, metaclass=EnumMeta):
    """Enum with a pretty :meth:`__str__` and :meth:`__repr__`."""

@unique
class ATS_FILE_NAME(ModeEnum):
    X = 'X'
    obs = 'obs.parquet'
    var = 'var.parquet'
    obsm = 'obsm'
    varm = 'varm'
    uns = 'uns'
    layers = 'layers'
    raw = 'raw'


@unique 
class DTYPE(PrettyEnum):
    # check for edianess
    float16 = np.dtype(np.float16).str
    float32 = np.dtype(np.float32).str
    float64 = np.dtype(np.float64).str
    int8 = np.dtype(np.int8).str
    int16 = np.dtype(np.int16).str
    int32 = np.dtype(np.int32).str
    int64 = np.dtype(np.int64).str
    uint8 = np.dtype(np.uint8).str
    uint16 = np.dtype(np.uint16).str
    uint32 = np.dtype(np.uint32).str
    uint64 = np.dtype(np.uint64).str

def save_X(
    X: Union[scipy.sparse.spmatrix, np.ndarray], 
    output_path: Union[str, os.PathLike], 
    chunk_size: int = 100, 
    dtype: DTYPE = None
):
    """
    Save a matrix to a tensorstore.

    :param X: The matrix to save.
    :param output_path: The path to the tensorstore.
    :param chunk_size: The chunk size to write.
    :param dtype: The data type to save.
    """
    dataset = ts.open({
        'driver': 'zarr',
        'kvstore': {
            'driver': 'file',
            'path': output_path,
        },
        'metadata': {
            'dtype': X.dtype.str if dtype is None else dtype,
            'shape': X.shape
        },
    }, create=True, delete_existing=True).result()

    if scipy.sparse.issparse(X):
        for e in range(0,X.shape[0],chunk_size):
            towrite = X[e:e+chunk_size].toarray()
            if dtype is not None:
                towrite = towrite.astype(dtype)
            write_future = dataset[e:min(X.shape[0], e+chunk_size), :].write(towrite)
            write_result = write_future.result()
    else:
        write_future = dataset.write(X)
        write_result = write_future.result()

def concat_and_save_X(
    X2: Union[scipy.sparse.spmatrix, np.ndarray], 
    output_path: Union[str, os.PathLike],
    chunk_size: int = 100
):
    dataset = ts.open({
        'driver': 'zarr',
        'kvstore': {
            'driver': 'file',
            'path': output_path,
        }
    })

    if dataset.shape[0] != X2.shape[0] and dataset.shape[1] == X2.shape[1]:
        # Determine the original and new shapes
        original_rows = dataset.shape[0]
        new_rows = original_rows + X2.shape[0]
        new_shape = (new_rows, dataset.shape[1])

        # Resize the dataset to accommodate additional rows
        dataset = dataset.resize(new_shape).result()

        # Write X2 to the expanded portion of the dataset
        if scipy.sparse.issparse(X2):
            for e in range(0, X2.shape[0], chunk_size):
                write_future = dataset[original_rows + e : original_rows + e + chunk_size, :].write(X2[e : e + chunk_size].toarray())
                write_result = write_future.result()
        else:
            write_future = dataset[original_rows:new_rows, :].write(X2)
            write_result = write_future.result()
    elif dataset.shape[0] == X2.shape[0] and dataset.shape[1] != X2.shape[1]:
        # Determine the original and new shapes
        original_cols = dataset.shape[1]
        new_cols = original_cols + X2.shape[1]
        new_shape = (dataset.shape[0], new_cols)

        # Resize the dataset to accommodate additional columns
        dataset = dataset.resize(new_shape).result()

        # Write X2 to the expanded portion of the dataset
        if scipy.sparse.issparse(X2):
            for e in range(0, X2.shape[1], chunk_size):
                write_future = dataset[:, original_cols + e : original_cols + e + chunk_size].write(X2[:, e : e + chunk_size].toarray())
                write_result = write_future.result()
        else:
            write_future = dataset[:, original_cols:new_cols].write(X2)
            write_result = write_future.result()
    else:
        raise ValueError("The shapes of the two matrices do not match, not supported yet")

def load_X(
    input_path: Union[str, os.PathLike], 
    obs_indices: Union[slice, np.ndarray] = None,
    var_indices: Union[slice, np.ndarray] = None,
    show_progress: bool = False,
    chunk_size: int = 1024,
    to_sparse: bool = True,
    sparse_format: Callable = scipy.sparse.csr_matrix
) -> Union[np.ndarray, scipy.sparse.spmatrix]:
    """
    Load a matrix from a tensorstore.

    :param input_path: The path to the tensorstore.
    :param obs_indices: The row indices to load.
    :param var_indices: The column indices to load.
    :param show_progress: Whether to show a progress bar.
    :param chunk_size: The chunk size to read.
    :param to_sparse: Whether to return a sparse matrix.
    :param sparse_format: The sparse matrix format to use
    
    :return: The matrix.
    """
    dataset = ts.open({
        'driver': 'zarr',
        'kvstore': {
            'driver': 'file',
            'path': input_path,
        }
    }, create=False).result()
    
    if obs_indices is None and var_indices is None:
        handler = dataset
    elif obs_indices is not None and var_indices is None:
        handler = dataset[obs_indices, :]
    elif obs_indices is None and var_indices is not None:
        handler = dataset[:, var_indices]
    else:
        handler = dataset[obs_indices, :][:, var_indices]

    Xs = []
    if show_progress:
        pbar = tqdm.tqdm(
            total=handler.shape[0],
            desc="Loading data", 
            bar_format='{l_bar}{bar:10}{r_bar}{bar:-10b}',
            position=0, 
            leave=True
        )
    for e in range(0, handler.shape[0], chunk_size):
        x = handler[e:min(handler.shape[0], e+chunk_size)].read().result()
        if len(x.shape) == 1:
            x = x.reshape(-1, 1)
        if to_sparse:
            Xs.append(sparse_format(x))
        else:
            Xs.append(x)
        if show_progress:
            pbar.update(chunk_size)
    if show_progress:
        pbar.close()
    if to_sparse:
        X = scipy.sparse.vstack(Xs)
    else:
        X = np.vstack(Xs)
    return X

def save_np_array_to_tensorstore(
    Z: np.ndarray, 
    output_path: Union[str, os.PathLike]
):
    """
    Save a numpy array to a tensorstore.

    :param Z: The numpy array to save.
    :param output_path: The path to the tensorstore.
    """
    dataset = ts.open({
        'driver': 'zarr',
        'kvstore': {
            'driver': 'file',
            'path': output_path,
        },
        'metadata': {
            'dtype': Z.dtype.str,
            'shape': Z.shape
        },
    }, create=True).result()
    
    write_future = dataset.write(Z)
    write_result = write_future.result()


def load_np_array_from_tensorstore(
    input_path: Union[str, os.PathLike], 
    obs_indices: Union[slice, np.ndarray] = None
) -> np.ndarray:
    """
    Load a numpy array from a tensorstore.

    :param input_path: The path to the tensorstore.
    :param obs_indices: The row indices to load.
    """
    dataset = ts.open({
        'driver': 'zarr',
        'kvstore': {
            'driver': 'file',
            'path': input_path,
        }
    }, create=False).result()

    if obs_indices is None:
        return dataset.read().result()
    else:
        return dataset[obs_indices].read().result()


def check_is_parquet_serializable(obj: pd.DataFrame):
    for c in obj.columns:
        if obj[c].dtype == 'O':
            obj[c] = obj[c].astype(str)


def save_anndata_to_tensorstore(
    adata: AnnData,
    output_path: str,
    is_raw_count: bool = False
):
    """
    Save an AnnData object to a tensorstore.

    :param adata: The AnnData object to save.
    :param output_path: The path to the tensorstore.
    :param is_raw_count: Whether the AnnData object is raw count data. 
                         If True, the raw count matrix will be saved as uint32 for memory efficiency.

    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    if hasattr(adata, 'X') and adata.X is not None:
        save_X(adata.X, os.path.join(output_path, 'X'), dtype=DTYPE.uint32 if is_raw_count else None)

    if hasattr(adata, 'obs') and adata.obs is not None:
        check_is_parquet_serializable(adata.obs)
        adata.obs.to_parquet(os.path.join(output_path, 'obs.parquet'))

    if hasattr(adata, 'var') and adata.var is not None:
        check_is_parquet_serializable(adata.var)
        adata.var.to_parquet(os.path.join(output_path, 'var.parquet'))

    if hasattr(adata, 'obsm') and adata.obsm is not None:
        for k, v in adata.obsm.items():
            save_np_array_to_tensorstore(v, os.path.join(output_path, f'obsm/{k}'))

    if hasattr(adata, 'varm') and adata.varm is not None:
        for k, v in adata.varm.items():
            save_np_array_to_tensorstore(v, os.path.join(output_path, f'varm/{k}'))

    if not os.path.exists(os.path.join(output_path, 'uns')):
        os.makedirs(os.path.join(output_path, 'uns'))

    if hasattr(adata, 'uns') and adata.uns is not None:
        for k, v in adata.uns.items():
            if isinstance(v, pd.DataFrame):
                check_is_parquet_serializable(v)
                v.to_parquet(os.path.join(output_path, f'uns/{k}.parquet'))
            else:
                with open(os.path.join(output_path, f'uns/{k}.pickle'), 'wb') as f:
                    pickle.dump(v, f)

    if adata.layers is not None:
        for k, v in adata.layers.items():
            save_X(v, os.path.join(output_path, f'layers/{k}'))

    if adata.raw is not None:
        save_anndata_to_tensorstore(adata.raw, os.path.join(output_path, 'raw'))

class PreviewObject:
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return str(self.obj)

    def __repr__(self):
        return self.obj

def preview_anndata_from_tensorstore(
    input_path: str,
):
    obs = pd.read_parquet(os.path.join(input_path, 'obs.parquet'))
    var = pd.read_parquet(os.path.join(input_path, 'var.parquet'))
    return PreviewObject(
           "AnnData object with n_obs × n_vars = {} × {}".format(obs.shape[0], var.shape[0]) + '\n' + \
           "    obs: {}".format(', '.join(obs.columns)) + '\n' + \
           "    var: {}".format(', '.join(var.columns)) + '\n'
    )

def load_anndata_from_tensorstore(
    input_path: str, 
    obs_indices: Union[slice, np.ndarray] = None,
    var_indices: Union[slice, np.ndarray] = None,
    obs_selection: List[Tuple[str, Any]] = None,
    var_selection: List[Tuple[str, Any]] = None,
    obs_names: List[str] = None,
    var_names: List[str] = None,
    as_sparse: bool = False
):
    """
    Load an AnnData object from a tensorstore.

    :param input_path: The path to the tensorstore.
    :param obs_indices: The row indices to load.
    :param var_indices: The column indices to load.
    :param var_names: The variable names to load.
    """

    if obs_names is not None:
        obs = pd.read_parquet(os.path.join(input_path, 'obs.parquet'))
        if obs_indices is not None:
            print("Warning: obs_names will override obs_indices")
        obs_indices = obs.index.isin(obs_names)

    if var_names is not None:
        var = pd.read_parquet(os.path.join(input_path, 'var.parquet'))
        if var_indices is not None:
            print("Warning: var_names will override var_indices")
        var_indices = var.index.isin(var_names)
    
    if var_indices is None and var_selection is not None:
        var_indices = np.zeros(_X.shape[1], dtype=bool)
        for k, v in var_selection:
            if isinstance(v, list):
                var_indices = var_indices | np.array(pd.Series(var[k]).isin(v))
            else:
                var_indices = var_indices | np.array((var[k] == v).values)

    if obs_indices is None and obs_selection is not None:
        obs = pd.read_parquet(os.path.join(input_path, 'obs.parquet'))
        obs_indices = np.zeros(obs.shape[0], dtype=bool)
        for k, v in obs_selection:
            if isinstance(v, list):
                obs_indices = obs_indices | np.array(pd.Series(obs[k]).isin(v))
            else:
                obs_indices = obs_indices | np.array((obs[k] == v).values)

    _X = load_X(os.path.join(input_path, 'X'), obs_indices, var_indices)
    if as_sparse:
        _X = scipy.sparse.csr_matrix(_X)

    if os.path.exists(os.path.join(input_path, 'obs.parquet')):
        obs = pd.read_parquet(os.path.join(input_path, 'obs.parquet'))
        # if obs_indices is a slice
        if isinstance(obs_indices, slice):
            _obs = obs.iloc[obs_indices]
        # if obs_indices is a array
        elif isinstance(obs_indices, np.ndarray):
            # if obs_indices is a boolean array
            if obs_indices.dtype == bool:
                _obs = obs.loc[obs_indices]
            elif obs_indices.dtype ==  int:
                _obs = obs.iloc[obs_indices]
            else:
                raise ValueError(f'Invalid obs_indices of type {type(obs_indices)} with value {type(obs_indices)}')
        elif isinstance(obs_indices, list):
            if isinstance(obs_indices[0], str) or isinstance(obs_indices[0], bool):
                _obs = obs.loc[obs_indices]
            elif isinstance(obs_indices[0], int):
                _obs = obs.iloc[obs_indices]
            else:
                raise ValueError(f'Invalid obs_indices of type {type(obs_indices[0])} with value {type(obs_indices[0])}')
        elif obs_indices is None:
            _obs = obs
        else:
            raise ValueError(f'Invalid obs_indices of type {type(obs_indices)}')
    
    if os.path.exists(os.path.join(input_path, 'var.parquet')):
        var = pd.read_parquet(os.path.join(input_path, 'var.parquet'))
        # if var_indices is a slice
        if isinstance(var_indices, slice):
            _var = var.iloc[var_indices]
        # if var_indices is a array
        elif isinstance(var_indices, np.ndarray):
            # if var_indices is a boolean array
            if var_indices.dtype == bool:
                _var = var.loc[var_indices]
            elif var_indices.dtype ==  int:
                _var = var.iloc[var_indices]
            else:
                raise ValueError(f'Invalid var_indices of type {type(var_indices)} with value {type(var_indices)}')
        elif isinstance(var_indices, list):
            if isinstance(var_indices[0], str) or isinstance(var_indices[0], bool):
                _var = var.loc[var_indices]
            elif isinstance(var_indices[0], int):
                _var = var.iloc[var_indices]
            else:
                raise ValueError(f'Invalid var_indices of type {type(var_indices[0])} with value {type(var_indices[0])}')
        elif var_indices is None:
            _var = var
        else:
            raise ValueError(f'Invalid var_indices of type {type(var_indices)}')
        
    _obsm = None
    if os.path.exists(os.path.join(input_path, 'obsm')):
        _obsm = {}
        for f in os.listdir(os.path.join(input_path, 'obsm')):
            _obsm[f] = load_np_array_from_tensorstore(os.path.join(input_path, 'obsm', f), obs_indices)

    _varm = None
    if os.path.exists(os.path.join(input_path, 'varm')):
        _varm = {}
        for f in os.listdir(os.path.join(input_path, 'varm')):
            _varm[f] = load_np_array_from_tensorstore(os.path.join(input_path, 'varm', f), var_indices)

    _uns = None
    if os.path.exists(os.path.join(input_path, 'uns')):
        _uns = {}
        for fname in os.listdir(os.path.join(input_path, 'uns')):
            if fname.endswith('.parquet'):
                _uns[fname[:-8]] = pd.read_parquet(os.path.join(input_path, 'uns', fname))
            elif fname.endswith('.pickle'):
                with open(os.path.join(input_path, 'uns', fname), 'rb') as f:
                    _uns[fname] = pickle.load(f)

    _layers = None
    if os.path.exists(os.path.join(input_path, 'layers')):
        _layers = {}
        for f in os.listdir(os.path.join(input_path, 'layers')):
            _layers[f] = load_X(os.path.join(input_path, 'layers', f), obs_indices, var_indices)

    adata = AnnData(
        X=_X,
        obs=_obs,
        var=_var,
        obsm=_obsm,
        varm=_varm,
        uns=_uns,
        layers=_layers
    )
    if os.path.exists(os.path.join(input_path, 'raw')):
        adata.raw = load_anndata_from_tensorstore(
            os.path.join(input_path, 'raw'), 
            obs_indices, 
            var_indices
        )

    return adata
