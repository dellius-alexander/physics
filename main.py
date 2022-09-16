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
fx, fy = symbols('fx, fy', cls=Function)

init_printing(use_unicode=True)


##########################################################################
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    values = m3d.variables_3d()
    # variables: {'R': 90, 'g': 9.8, 'y_0': 0, 'x_0': 0, 'angle': 70})
    # values['R'] = 20
    # values['g'] = 10.0
    # values['y_0'] = 0
    # values['x_0'] = 0
    # values['angle'] = 45
    # values['t'] = 2
    # values['y'] = 20
    # # print(converter.dict_to_json_string(values))
    # # values = m3d.
    # values = m3d.horizontal_range(values)
    # values = m3d.trajectory(values)
    # values = m3d.time_of_flight(values)
    # print(converter.dict_to_json_string(values))
    ######################################################################
    # values = {'v_y': 0,  # v_y**2
    #           'v_0y': v_0y,  # v_0y**2
    #           'g': 9.8,
    #           'y': y,
    #           'y_0': 0,
    #           'v': v,
    #           'v_0': 70,
    #           'v_x': v_x,  # v_y**2
    #           'v_0x': v_0x,  # v_0y**2
    #           'x': x,
    #           'x_0': 0,
    #           't': t,
    #           'angle': 75,
    #           'i': i,
    #           'j': j,
    #           'k': k,
    #           's': s
    #           }
    # fy = -v_y + v_0y - 2 * g * (y - y_0)

    # values = {'v_y': v_y,  # v_y**2
    #           'v_0y': v_0y,  # v_0y**2
    #           'g': 9.8,
    #           'y': 10,
    #           'y_0': 0,
    #           'v': v,
    #           'v_0': 30,
    #           'v_x': v_x,  # v_y**2
    #           'v_0x': v_0x,  # v_0y**2
    #           'x': x,
    #           'x_0': 0,
    #           't': t,
    #           'angle': 45,
    #           'i': i,
    #           'j': j,
    #           'k': k
    #           }
    # fy = y_0 - y + v_0y * t - (1 / 2) * g * (t ** 2)

    # fx = x_0 - x - v_x * t
    # sol = m3d.projectile(xfunc=fx, yfunc=fy, values=values)
    # jsn = converter.dict_to_json_string(sol)
    # print(jsn)
    ######################################################################
    # f = -y + y_0 + (1/2) * (v_0y + v_y) * t
    # f = -v_y + v_0y - g * t
    # f = - (v_y ** 2) + (v_0y ** 2) - 2 * g * (y - y_0)
    f = -R + ((v_0 ** 2) * sin(2 * theta)) / g
    f = solve(f, v_0)
    pprint(f)

    values['g'] = 10.0
    # values['angle'] = 45
    # values['v_y'] = 0
    # values['v_x'] = 20
    values['t'] = 2
    values['x_0'] = 0
    values['x'] = 15.25
    values['y_0'] = 3.05
    values['y'] = 0
    values['v_y'] = 0

    values = m3d.projectile(values)
    values = m3d.horizontal_range(values)
    values = m3d.trajectory(values)
    values = m3d.time_of_flight(values)
    pprint(converter.dict_to_json_string(values))
    # cnt = 0.0
    # for n, a in enumerate(range(0, 20)):
    #     ans = values['y'].subs({'x': a - a + cnt})
    #     print(cnt, ans)
    #     cnt += 0.1

