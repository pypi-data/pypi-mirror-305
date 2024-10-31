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

r"PyCI RDMs tools set."

import numpy as np


__all__ = [
    "flat_tensor",
]



def flat_tensor(tensor, shape):
    r"""
    Flat arbitrary dimentsion tensor into a matrix

    Parameters
    ----------
    tensor : np.ndarray
        Tensor to be reshaped.
    shape : tuple
        Final shape of the matrix

    Returns
    -------
    np.ndarray
    """

    return np.reshape(tensor, shape)
