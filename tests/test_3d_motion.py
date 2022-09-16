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
# from physics.utils import converter
from physics.motion_3d import motion_3d as m3d
from sympy import symbols


##########################################################################
# GLOBAL Symbols
##########################################################################
def test_3d_motion():
    values = m3d.variables_3d()
    x = symbols('x')
    # variables: {'R': 90, 'g': 9.8, 'y_0': 0, 'x_0': 0, 'angle': 70})
    values['g'] = 9.8
    values['y_0'] = 0
    values['x_0'] = 0
    values['angle'] = 70
    values['R'] = 90
    # print(converter.dict_to_json_string(values))
    values = m3d.horizontal_range(values)
    values = m3d.trajectory(values)
    values = m3d.time_of_flight(values)
    print(values)
    # print(converter.dict_to_json_string(values))
    assert values['v_0'] == 37.0425217188420
    assert values['y'] == (- 0.0305275268828291 * (x ** 2) + 2.74747741945462 * x)
    values = m3d.variables_3d()
    values['R'] = 90
    values['g'] = 9.8
    values['y_0'] = 0
    values['x_0'] = 0
    values['angle'] = 30
    values = m3d.horizontal_range(values)
    values = m3d.trajectory(values)
    values = m3d.time_of_flight(values)
    print(values)
    # print(converter.dict_to_json_string(values))
    assert values['v_0'] == 31.9130987973669
    assert values['y'] == (- 0.00641500299099584 * (x ** 2) + 0.577350269189626 * x)
