# This file is part of PyCI.
#
# PyCI is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# PyCI is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyCI. If not, see <http://www.gnu.org/licenses/>.

r"""PyCI Griebel-Knapek CI module."""

from . import pyci


__all__ = [
    "add_cost",
]



def add_cost(wfn, cost, q_max, t=-0.5):
    r"""
    Add determinants to the wave function according to the odometer algorithm
    (Griebel-Knapeck CI) [GKCI1]_.

    .. [GKCI1] Anderson, James SM, Farnaz Heidar-Zadeh, and Paul W. Ayers. "Breaking the curse of
               dimension for the electronic Schrödinger equation with functional analysis."
               *Computational and Theoretical Chemistry* 1142 (2018): 66-77.

    Parameters
    ----------
    wfn : pyci.wavefunction
        Wave function.
    cost : np.ndarray
        Orbital energies. 
    q_max: float
        Maximum cost of selected determinant
    t : float, default=-0.5
        Smoothness factor.

    """
    # Run odometer algorithm
    if isinstance(wfn, (pyci.doci_wfn, pyci.genci_wfn)):
        pyci.odometer_one_spin(wfn, cost, q_max=q_max, t=t)
    elif isinstance(wfn, pyci.fullci_wfn):
        pyci.odometer_two_spin(wfn, cost, q_max=q_max, t=t)
    else:
        raise TypeError(f"invalid `wfn` type `{type(wfn)}`; must be `pyci.wavefunction`")
