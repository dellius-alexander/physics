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
from typing import List, Set, Dict, Tuple, Optional, Any
from sympy import init_printing, symbols, sqrt, \
    Function, Number, pprint, solve, Symbol, sin, cos, \
    rad, tan
import re
import mpmath as mp
import sys
import types
from physics.utils.converter import dict_to_json_string

##########################################################################
init_printing(use_unicode=True)


##########################################################################
# GLOBAL Symbols

##########################################################################
def acceleration_vector(func=Function, sym=Symbol, time=Number):
    try:
        derivative = func.diff(sym.expr_free_symbols)
        direction = derivative.subs(sym, time)
        magnitude = magnitude_func(direction, 2)
        print("\n######################################################################")
        print("\nAcceleration Vector: ")
        pprint(derivative)
        print("\nMagnitude of Acceleration: \n")
        pprint(magnitude)
        print("\n######################################################################")
    except Exception as e:
        tb = sys.exc_info()
        print(type(e))  # the exception instance
        print(e.args)  # arguments stored in .args
        print(e)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
        print(f'args = {e.args}')  # unpack args
        print(f'Something went wrong with: \n{tb}')
    ######################################################################


##########################################################################
def magnitude_func(func=Function or list, p=2):
    """
    Gets the magnitude from the given function.

    :param p: p = power defaults to 2
    :param func: f(x)
    :return: the magnitude of displacement of the position function, i, j and k
    """
    fk = []
    magnitude = 0
    pprint(func)
    for n in func.__str__().split():
        pprint(n)
        if re.compile(r'^[0-9]*[.]{0,1}[0-9]*$').match(n):
            fk.append(n)
        elif re.compile(r'^([0-9.]*[*]{1}[a-zA-Z]{1})$').match(n):
            for a in n.split('*'):
                if re.compile(r'^[0-9]*[.]{1}[0-9]*$').match(a) and a != " " and not re.compile(
                        r'(\+|-|/|I|J|K|i|j|k)').match(a):
                    fk.append(f"{a}**{p}")
                else:
                    fk.append(a)
            print(fk)
        else:
            fk.append(n)
    ######################################################################
    for a in fk:
        if not a.isalpha() and not re.compile(r'(\+|-|/|I|J|K|i|j|k)').match(a):
            print(a)
            a = a
            magnitude += eval(str(a))
    print(magnitude)
    magnitude = abs(sqrt(magnitude))
    # print(f'\nMagnitude: {magnitude}')
    return magnitude


##########################################################################
def init_y_velocity(velocity, degree):
    try:
        return velocity * mp.sin(mp.radians(degree))
    except Exception as e:
        tb = sys.exc_info()
        print(type(e))  # the exception instance
        print(e.args)  # arguments stored in .args
        print(e)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
        print(f'args = {e.args}')  # unpack args
        print(f'Something went wrong with: \n{tb}')


##########################################################################
def vertical_displacement(values: Dict = None):
    # v_0y
    if isinstance(values['v_0y'], Symbol):
        values['v_0y'] = values['v_0y'].subs(values)
        if isinstance(values['v_0y'], Symbol):
            values['v_0y'] = values['v_y'] * mp.sin(mp.radians(values['angle']))
        if isinstance(values['v_0y'], Symbol):
            values['v_0y'] = values['g'] * values['t'] + values['v_y']
        if isinstance(values['v_0y'], Symbol):
            values['v_0y'] = (values['t'] * values['v_y'] +
                              2.0 * values['y'] - 2.0 * values['y_0']) / values['t']
        if isinstance(values['v_0y'], Symbol):
            values['v_0y'] = (values['t'] * values['v_y'])
        if isinstance(values['v_0y'], Symbol):
            values['v_0y'] = sqrt(2.0 * values['g'] * values['y'] - 2.0 *
                                  values['g'] * values['y_0'] + (values['v_y'] ** 2))

    # v_0
    if isinstance(values['v_0'], Symbol):
        values['v_0'] = values['v_0'].subs(values)
        if isinstance(values['v_0'], Symbol):
            values['v_0'] = values['v_0y'] / mp.sin(mp.radians(values['angle']))
        if isinstance(values['v_0'], Symbol):
            values['v_0'] = values['v_x'] / mp.cos(mp.radians(values['angle']))

    # y
    if isinstance(values['y'], Symbol):
        values['y'] = values['y'].subs(values)
        if isinstance(values['y'], Symbol):
            values['y'] = sqrt((values['v_y'] ** 2) / (2 * values['g']))
        # if isinstance(values['y'], Symbol):
        #     values['y'] = sqrt((values['v_0y'] ** 2) / (2 * values['g']))

    # t
    if isinstance(values['t'], Symbol):
        values['t'] = values['t'].subs(values)
        if isinstance(values['t'], Symbol):
            values['t'] = (2.0 * (values['y'] - values['y_0'])) / (values['v_0y'] + values['v_y'])
        if isinstance(values['t'], Symbol):
            values['t'] = values['v_0y'] / values['g']

    # v_y
    if isinstance(values['v_y'], Symbol):
        values['v_y'] = values['v_y'].subs(values)
        if isinstance(values['v_y'], Symbol):
            values['v_y'] = values['v_0y'] - values['g'] * values['t']

    if values['counter'] < 300:
        values['counter'] += values['counter'] + 1
        return vertical_displacement(values)
    return values


##########################################################################
def horizontal_displacement(values={}):
    # print(__values)
    if isinstance(values['v_0'], Number) and isinstance(values['angle'], (Number, float)):
        values['v_x'] = values['v_0'] * mp.cos(mp.radians(values['angle']))
    if isinstance(values['v_0'], (Number, float)) and isinstance(values['angle'], (Number, float)):
        values['v_x'] = values['v_x'] / values['t']
    if isinstance(values['x'], Symbol):
        values['x'] = values['x_0'] + values['v_x'] * values['t']
    if values['counter'] < 300:
        values['counter'] += values['counter'] + 1
        return projectile(values)
    return values


##########################################################################
def projectile(
        values={}):
    """
    Solver for projectile motion.

    :param values: a map of linear components
    :return:
    """
    # print(dict_to_json_string(values))
    values = update_map(
        vertical_displacement(values),
        values)
    # print(dict_to_json_string(values))
    # log.info("\n%s", dict_to_json_string(values))
    values = update_map(
        horizontal_displacement(values),
        values)
    if isinstance(values['v_y'], Number) and isinstance(values['v_x'], Number) \
            and isinstance(values['v'], Symbol):
        values['v'] = sqrt((values['v_x'] ** 2) + (values['v_y'] ** 2))
        values['theta_v'] = direction(values['v_x'], values['v_y'])  # direction of r
    if isinstance(values['y'], Number) and isinstance(values['x'], Number):
        values['r'] = sqrt((values['x'] ** 2) + (values['y'] ** 2))
        values['theta_r'] = direction(values['x'], values['y'])  # direction of r
    # values['v_0x'] = values['v_x']
    # return if we ready
    if isinstance(values['x'], Number) and isinstance(values['y'], Number) \
            and isinstance(values['v'], Number) and isinstance(values['v_0x'], Number) \
            and isinstance(values['v_0y'], Number):
        return values
    if values['counter'] < 300:
        values['counter'] += values['counter'] + 1
        return projectile(values)
    return values


##########################################################################
def direction(xz, y):
    """
    Gets the direction of Θ:

    - Θ = tan^(−1) ⁡(y/x)

    - Θ = tan^(−1) ⁡(z/x)

    :param xz: x or z value
    :param y: y value
    :return: direction in radians and degrees
    """
    try:
        print(f'\nxz: {xz}, y: {y}\n')
        theta = mp.atan(y / xz)
        # print(f"\nΘ = {theta}")
        return {"rad": theta, "deg": mp.degrees(theta)}
    except Exception as e:
        tb = sys.exc_info()
        print(type(e))  # the exception instance
        print(e.args)  # arguments stored in .args
        print(e)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
        print(f'args = {e.args}')  # unpack args
        print(f'Something went wrong with: \n{tb}')


##########################################################################
def update_map(map1={}, map2={}):
    """
    map1
    :param map1:
    :param map2:
    :return:
    """
    try:
        for n, m in zip(map1.keys(), map1.values()):
            for p, q in zip(map2.keys(), map2.values()):
                if n.__eq__(p) and m != q:
                    map2[f'{n}'] = m
        return map2
    except Exception as e:
        tb = sys.exc_info()
        print(type(e))  # the exception instance
        print(e.args)  # arguments stored in .args
        print(e)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
        print(f'args = {e.args}')  # unpack args
        print(f'Something went wrong with: \n{tb}')


##########################################################################
def time_of_flight(values={}):
    if isinstance(values['tof'], Symbol) \
            and isinstance(values['v_0'], Number) \
            and isinstance(values['angle'], Number) \
            and isinstance(values['g'], Number):
        values['tof'] = (2 * (values['v_0'] * mp.sin(values['angle']))) / values['g']
        print("\nTime of Flight:=> TOF =  ")
        values['tof'] = values['tof'].subs(values)
        print(values['tof'])
    if values['counter'] < 300 \
            and isinstance(values['tof'], Symbol):
        values['counter'] += values['counter'] + 1
        values['tof'] = values['tof'].subs(values)
        time_of_flight(values)
    return values


##########################################################################
def trajectory(values={}):
    if not isinstance(values['y'], Symbol):
        values['y'] = (mp.tan(mp.radians(values['angle'])) * values['x']) - (values['g'] /
                                                                             (2 * (values['v_0'] * mp.cos(
                                                                                 mp.radians(
                                                                                     values['angle']))) ** 2)) * (
                              values['x'] ** 2)
        if isinstance(values['y'], Symbol):
            print("\nTrajectory:=> y =  ")
            values['y'] = values['x'] * (tan(mp.radians(values['angle'])) -
                                         (values['g'] / (
                                                 2 * ((values['v_0'] * cos(mp.radians(values['angle']))) ** 2))) *
                                         values['x'])
        if isinstance(values['y'], Number):
            print("\nTrajectory:=> y =  ")
            pprint(values['y'])
    if values['counter'] < 300 and isinstance(values['y'], Symbol):
        values['y'] = values['y'].subs(values)
    return values


##########################################################################
def horizontal_range(values={}):
    values['v_0'] = sqrt((values['R'] * values['g']) / mp.sin(2 * mp.radians(values['angle'])))
    if isinstance(values['v_0'], Symbol):
        values['v_0'] = sqrt((values['R'] * values['g']) / mp.sin(2 * mp.radians(values['angle'])))
        if isinstance(values['v_0'], Number):
            values['v_0'] = round(values['v_0'], 6)
            print("Solving for v_0:")
            print('\nInitial velocity:=> v_0 =')
            print(dict_to_json_string(values['v_0']))
    if isinstance(values['v_0'], Number) and isinstance(values['angle'], Number):
        values['R'] = ((values['v_0'] ** 2) * mp.sin(2 * mp.radians(values['angle']))) / values['g']
        if isinstance(values['R'], Number):
            values['R'] = round(values['R'], 6)
            print("Solving for R: ")
            print('\nRange :=> R =')
            print(dict_to_json_string(values['R']))
    if values['counter'] < 300:
        values['counter'] += values['counter'] + 1
        return horizontal_range(values)
    values['counter'] = 1
    return values


##########################################################################
def variables_3d() -> dict:
    x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, theta = \
        symbols('x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, '
                'theta', cls=Symbol)
    return dict({
        'R': R,  # range
        'r': r,
        'g': g,
        'x': x,
        'x_0': x_0,
        'y': y,
        'y_0': y_0,
        'z': z,
        'z_0': z_0,
        'v': v,
        'v_0': v_0,
        'v_x': v_x,  # v_y**2
        'v_0x': v_0x,  # v_0y**2
        'v_y': v_y,  # v_y**2
        'v_0y': v_0y,  # v_0y**2
        'i': i,
        'j': j,
        'k': k,
        't': t,
        'angle': theta,  # angle of elevation
        'tof': tof,
        'theta': theta,
        'counter': 0
    })


##########################################################################
def collection(__equations__: Dict,
               find: Optional[Symbol or str] = None,
               solve_f: Optional[Symbol or str] = None
               ):
    fd, sf = symbols(f'{find}, {solve_f}', cls=Symbol)
    d = {fd: sf}
    solutions = []
    for n, val in enumerate(__equations__[f'{fd}']):
        if isinstance(val, list):
            for item in val:
                # check for numbers
                if isinstance(item, Number):
                    ans = item
                else:
                    ans = solve(item, d)
                # check for solutions
                if len(ans) == 0:
                    continue
                else:
                    solutions.append(ans)
        else:
            ans = solve(val, d)
            if len(ans) == 0:
                continue
            else:
                solutions.append(ans)
    return dict_to_json_string({sf: solutions})


##########################################################################
def equations(find_var: Optional[str] = None,
              solve_for: Optional[str] = None,
              options: Optional[List[str]] = ['list', 'solve'] or None) -> Dict:
    """
    A collection of equations and algorithms for solving projectile motion lemma's.

    - Given:  y = y_0 + (1/2) * (v_0y + v_y) * t

        - first we find an equation with the given variable as a component: v_y,
        - solves for the solution: v_0y,
        - by default will attempt to solve for v_0y

    :param find_var: the function or variable we want to solve for. This could also
        mean a function or variable found in an equation

    :param solve_for: the variable you are solving for.

    :param options: optional commands: ['solve','list','equation']; solve for
        solution=y_0, list all equations, provide a solution for the given
        function/equation. sometimes you just want a list or equations or
        just to solve for the equation,in such a case, the optoins offer
        some flexibility by providing an array
        of string keywords like: options=['solve','list','equation']
    :return: a dictionary of equations
    """
    x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, theta, \
        a_c, m, s = \
        symbols(f'x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, theta,'
                f'a_c, m, s', cls=Symbol)

    f, g, h, fx, fy, fz, gx, gy, gz, hx, hy, hz = symbols('f, g, h, f(x), f(y), f(z), g(x), g(y), '
                                                          'g(z), h(x), h(y), h(z)', cls=Function)
    __equations__ = dict({
        # vertical displacememt
        'y': [
            ['(-y + y_0) + (1/2) * (v_0y + v_y) * t'],
            ['(-y + y_0) + v_y * t - (1/2) * g * (t ** 2)'],
            ['(-y + 2 * g * y_0) + (v_0y ** 2) - (v_y ** 2) / (2 * g)'],
        ],
        # horizontal displacement
        'x': [
            ['(-x + x_0) + v_x * t']
        ],
        # initial horizontal velocity
        'v_0x': [
            ['v_x']
        ],
        # final horizontal velocity
        'v_x': [
            ['- v_x + v_0 * cos(theta)', 'v_0 * cos(theta) ']
        ],
        # centripetal acceleration
        # The direction of the acceleration vector is  toward the center of
        # the circle This is a radial acceleration and is called the centripetal
        # acceleration, which is why we give it the subscript c.
        'a_c': [
            ['(v ** 2) / r', '(v ** 2) / r - a_c']
        ],
        # acceleration due to gravity
        'g': [
            ['- g + (v ** 2) / r'],
            ['-g + 9.8 * (m/(s**2))'],
            ['-g + 10.0 * (m/(s**2))']
        ],
        # radius of the circle
        'r': [
            ['-r + (v ** 2) / a_c']
        ],
        # velocity: sqrt(a_c * r)
        'v': [
            ['-v + sqrt(a_c * r)']
        ]
    })
    ######################################################################
    # return map of equations
    if find_var is None and solve_for is None and options.__contains__('list'):
        return dict_to_json_string(__equations__)
    # list the equation that contain that variable find_var
    if find_var is not None and solve_for is None and options.__contains__('list'):
        return dict_to_json_string(collection(__equations__, find_var, find_var))
    # solves for the given equation defined in solve for
    if find_var is not None and solve_for is not None and options.__contains__('solve'):
        return collection(__equations__, find_var, solve_for)


##########################################################################

if __name__ == '__main__':
    print(dict_to_json_string(equations('g')))
