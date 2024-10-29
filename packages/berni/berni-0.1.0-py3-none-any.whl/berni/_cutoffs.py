import numpy as np
from .helpers import _objdict

__all__ = ['shift', 'cut', 'linear', 'quadratic',
           'quadratic_cut_shift', 'linear_cut_shift', 'cut_shift']

class shift:

    # def __init__(self, func, params, cutoff_params):
    #     cutoff_params['rcut'] = np.array(cutoff_params['rcut'])
    #     nsp = cutoff_params['rcut'].shape[0]
    #     cutoff_params['shift'] = np.ndarray((nsp, nsp))
    #     for isp in range(nsp):
    #         for jsp in range(nsp):
    #             cutoff_params['shift'][isp, jsp] = func(cutoff_params['rcut'][isp, jsp], isp, jsp, **params)[0]
    #     # Somehow jax only accepts a reference to a dict
    #     self._params = cutoff_params
    #     self._func = func

    def __init__(self, func, params, cutoff_params):
        cutoff_params['rcut'] = np.array(cutoff_params['rcut'])
        cutoff_params['shift'] = func(cutoff_params['rcut'], **params)[0]
        self._params = cutoff_params
        self._func = func

    def __call__(self, func):
        def wrapper(r, *args, **kwargs):
            return self._func(r, *args, **kwargs) - self._params['shift']
        wrapper._params = self._params
        return wrapper

class cut:
    pass

class linear:
    pass

class quadratic:
    pass

class cubic_spline:
    pass


cut_shift = shift
linear_cut_shift = linear
quadratic_cut_shift = quadratic
