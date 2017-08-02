"""
Copyright 2013 Steven Diamond

This file is part of CVXPY.

CVXPY is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

CVXPY is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with CVXPY.  If not, see <http://www.gnu.org/licenses/>.
"""

from cvxpy.atoms.affine.sum import sum
from cvxpy.expressions.variable import Variable


def sum_largest_canon(expr, args):
    x = args[0]
    k = expr.k
    shape = expr.shape

    # min sum(t) + kq
    # s.t. x <= t + q
    #      0 <= t
    t = Variable(x.shape)
    q = Variable()
    obj = sum(t) + k*q
    constraints = [x <= t + q, t >= 0]
    return obj, constraints
