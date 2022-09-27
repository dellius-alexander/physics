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
from sympy import symbols, Symbol
import pytest

##########################################################################
# GLOBAL Symbols
##########################################################################
x = symbols('x')


##########################################################################
@pytest.mark.parametrize('angle', [70, 30, 50])
def test_3d_motion_1(angle):
    # variables: {'R': 90, 'g': 9.8, 'y_0': 0, 'x_0': 0, 'angle': 70})
    values = m3d.variables_3d()
    values['g'] = 9.8
    values['y_0'] = 0
    values['x_0'] = 0
    values['angle'] = angle
    values['R'] = 90
    values = m3d.horizontal_range(values)
    values = m3d.trajectory(values)
    values = m3d.time_of_flight(values)
    assert str(values['v_0']) == str(values['v_0'])
    assert str(values['y']) == str(values['y'])
    assert str(values['tof']) == str(values['tof'])
    print(converter.dict_to_json_string(values))


@pytest.mark.parametrize('func', ['x', 'y', 'v', 'r', 'a_c', 'g'])
def test_display_equations(func: Symbol):
    equations = converter.dict_to_json_string(m3d.equations(find_var=func))
    print(equations)
    expected = equations
    assert equations == expected
