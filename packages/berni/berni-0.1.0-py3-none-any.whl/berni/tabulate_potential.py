# This file is part of atooms
# Copyright 2010-2017, Daniele Coslovich

"""Pair potential classes and factory."""

import warnings
import numpy


def tabulate(potential, npoints=10000, rmax=-1.0, rmin=0.0, overshoot=2, **kwargs):
    """
    Tabulate the potential from 0 to `rmax`.

    The potential cutoff is only used to determine `rmax` if this
    is not given. The full potential is tabulated, it is up to the
    calling code to truncate it. We slightly overshoot the
    tabulation, to avoid boundary effects at the cutoff or at
    discontinuities.
    """
    if hasattr(potential, '_params'):
        rmax = potential._params['rcut']
    assert rmax > 0, 'provide rmax'
    rsq = numpy.ndarray(npoints)
    u0 = numpy.ndarray(npoints)
    u1 = numpy.ndarray(npoints)
    u2 = numpy.ndarray(npoints)
    # We overshoot 2 points beyond rmax (cutoff) to avoid
    # smoothing discontinuous potentials.
    # This is necessary also for the Allen Tildesley lookup table,
    # which for any distance within the cutoff will look up two
    # points forward in the table.
    # Note that the cutoff is applied to the function only to smooth it
    # not to cut it.
    drsq = (rmax**2 - rmin**2) / (npoints - overshoot - 1)
    warnings.filterwarnings("ignore")
    for i in range(npoints):
        rsq[i] = rmin**2 + i * drsq
        # u0[i], u1[i], u2[i] = potential(rsq[i]**0.5)
        # u0[i], u1[i], u2[i] = potential(rsq[i])
        # print(rsq[i]**0.5, u0[i], u1[i], u2[i])
        try:
            u0[i], u1[i], u2[i] = potential(rsq[i]**0.5, **kwargs)
        except ZeroDivisionError:
            u0[i], u1[i], u2[i] = float('nan'), float('nan'), float('nan')
    warnings.resetwarnings()

    # For potentials that diverge at zero, we remove the singularity by hand
    import math
    if math.isnan(u0[0]):
        u0[0], u1[0], u2[0] = u0[1], u1[1], u2[0]
    return rsq, u0, u1, u2


# class PairPotential:

#     def _adjust(self):
#         """Adjust the cutoff to the potential."""
#         self._adjusted = True
#         if self.cutoff is not None and self.cutoff.radius > 0:
#             u = self.func(self.cutoff.radius**2, **self.params)
#             self.cutoff.tailor(self.cutoff.radius**2, u)

#     def compute(self, rsquare):
#         """Compute the potential and its derivatives."""
#         if not self._can_compute:
#             raise ValueError('cannot compute unknown potential %s' % self.func)

#         if not self._adjusted:
#             self._adjust()
#         # Compute the potential and smooth it via the cutoff
#         u = self.func(rsquare, **self.params)
#         if self.cutoff is not None:
#             u = self.cutoff.smooth(rsquare, u)
#         # if rsquare < self.hard_core**2:
#         #     u0, u1 = float("inf"), float("inf")
#         return u
