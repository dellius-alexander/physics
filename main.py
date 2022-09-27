##########################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# physics_2211  Copyright (C) 2022  Dellius Alexander
# This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
# This is free software, and you are welcome to redistribute it
# under certain conditions; type `show c' for details.
##########################################################################
from physics.utils import converter
from physics.motion_3d import motion_3d as m3d
from sympy import symbols, Function, Symbol, init_printing, pprint, \
    rad, vector, solve, sin, cos
import mpmath as m
from sympy.vector import CoordSys3D, Del, curl
##########################################################################
# GLOBAL Symbols
x, x_0, y, y_0, z, z_0, i, j, k, v_x, v_0x, v_y, v_0y, v, v_0, g, t, s, tof, theta, R, vec = \
    symbols('x, x_0, y, y_0, z, z_0, i, j, k, v_x, v_0x, v_y, v_0y, v, v_0, g, t, s, tof, theta, R, vec', cls=Symbol)
f, fx, fy = symbols('f, fx, fy', cls=Function)

init_printing(use_unicode=True)


##########################################################################
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
