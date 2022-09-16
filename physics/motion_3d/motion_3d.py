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

import sympy as sym
from sympy import init_printing, symbols, sqrt, \
    Function, Number, pprint, solve, Symbol, sin, cos, \
    rad, tan
import re
import mpmath as m
import sys
from ..utils.converter import dict_to_json_string

# from ..utils import __logger
#
# log = __logger.log("physics", '..logging.conf')
# # 'application' code
# log.debug('debug message')
# log.info('info message')
# log.warning('warn message')
# log.error('error message')
# log.critical('critical message')
##########################################################################
init_printing(use_unicode=True)


##########################################################################
# GLOBAL Symbols
# x, y, z, t, i, k, j, v, a, b, c, m, s, y_0, x_0, v_0y, v_0x, v_y, v_x, d, v__2_y, v__2_0y, g = \
# symbols('x, y, z, t, i, k, j, v, a, b, c, m, s, y_0, x_0, v_0y, v_0x, v_y, v_x, d, v__2_y, v__2_0y, g', cls=Symbol)
# f, h = symbols('f, h', cls=Function)


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


######################################################################


##########################################################################
def init_y_velocity(velocity, degree):
    try:
        return velocity * m.sin(m.radians(degree))
    except Exception as e:
        tb = sys.exc_info()
        print(type(e))  # the exception instance
        print(e.args)  # arguments stored in .args
        print(e)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
        print(f'args = {e.args}')  # unpack args
        print(f'Something went wrong with: \n{tb}')


##########################################################################
def vertical_displacement(func=Function,
                          __values={}
                          ):
    f = func
    # pprint(f'\nf(y) = {f}\n')
    for k, v in zip(__values.keys(), __values.values()):
        f = f.subs(k, v)
    if isinstance(__values['v_0y'], Symbol) and isinstance(__values['v_0'], (Number, float, int)):
        __values['v_0y'] = __values['v_0'] * m.sin(m.radians(__values['angle']))
    if isinstance(__values['y'], Symbol):
        __values['y'] = (__values['v_0y'] ** 2) / (2 * __values['g'])
    f = f.subs(__values)
    pprint(f)
    if len(solve(f, __values['t'])) != 0:
        __values['t'] = solve(f, __values['t'])[1]
    else:
        __values['t'] = __values['v_0y'] / __values['g']
    if isinstance(__values['v_y'], Symbol) and isinstance(__values['t'], (Number, float, int)):
        __values['v_y'] = __values['v_0y'] - __values['g'] * __values['t']
    return __values


##########################################################################
def horizontal_displacement(func=Function,
                            __values={}
                            ):
    f = func
    for k, v in zip(__values.keys(), __values.values()):
        f = f.subs(k, v)
    __values['v_x'] = __values['v_0'] * m.cos(m.radians(__values['angle']))
    __values['x'] = __values['v_x'] * __values['t']
    return __values


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
        theta = m.atan(y / xz)
        # print(f"\nΘ = {theta}")
        return {"rad": theta, "deg": m.degrees(theta)}
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
def projectile(
        xfunc=Function,
        yfunc=Function,
        values={}):
    """
    Solver for projectile motion.

    :param xfunc: f(x)
    :param yfunc: f(y)
    :param values: a map of linear components
    :return:
    """

    print("\nVertical component: ")
    pprint(yfunc)
    print("\nHorizontal component: ")
    pprint(xfunc)
    # print(dict_to_json_string(values))
    values = update_map(
        vertical_displacement(
            yfunc,
            __values=values),
        values)

    # log.info("\n%s", dict_to_json_string(values))
    values = update_map(
        horizontal_displacement(
            xfunc,
            __values=values),
        values)
    if isinstance(values['v_y'], (Number, float, int)) and values['v_y'] != 0 and \
            isinstance(values['v_x'], (Number, float, int)) and values['v_x'] != 0:
        f = values['v_x'] * values['i'] + values['v_y'] * values['j']
        # pprint(f)
        values['v'] = magnitude_func(func=f)  # magnitude of vector r
        values['\\theta_{v}'] = direction(values['v_x'], values['v_y'])  # direction of r
    if isinstance(values['y'], (Number, float, int)) and values['y'] != 0 and \
            isinstance(values['x'], (Number, float, int)) and values['x'] != 0:
        f = values['x'] * values['i'] + values['y'] * values['j']
        # pprint(f)
        values['s'] = magnitude_func(func=f)  # magnitude of vector r
        values['\\theta_{s}'] = direction(values['x'], values['y'])  # direction of r
    values['v_0x'] = values['v_x']
    # print(f"\nThe magnitude of the final velocity r is: {f}\n")
    # pprint(f)
    return values


##########################################################################
def time_of_flight(values={}):
    values['tof'] = (2 * (values['v_0'] * m.sin(values['angle']))) / values['g']
    print("\nTime of Flight:=> TOF =  ")
    values['tof'] = values['tof'].subs(values)
    pprint(values['tof'])
    return values


##########################################################################
def trajectory(values={}):
    values['y'] = (m.tan(m.radians(values['angle'])) * values['x']) - (values['g'] /
                  (2 * (values['v_0'] * m.cos(m.radians(values['angle']))) ** 2)) * (values['x'] ** 2)
    print("\nTrajectory:=> y =  ")
    values['y'] = values['y'].subs(values)
    pprint(values['y'])
    return values


##########################################################################
def horizontal_range(values={}):
    if not isinstance(values['R'], Symbol) and isinstance(values['v_0'], Symbol):
        values['v_0'] = sqrt((values['R'] * values['g']) / m.sin(2 * m.radians(values['angle'])))
        print("Solving for v_0:")
        print('\nInitial velocity:=> v_0 =')
        pprint(values['v_0'])
    elif isinstance(values['R'], Symbol) and not isinstance(values['v_0'], Symbol):
        values['R'] = ((values['v_0'] ** 2) * m.sin(2 * m.radians(values['angle']))) / values['g']
        print("Solving for R: ")
        print('\nRange :=> R =')
        pprint(values['R'])
    return values


##########################################################################
def variables_3d() -> dict:
    x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, theta = \
        symbols('x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, theta')
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
        'theta': theta
    })


##########################################################################

