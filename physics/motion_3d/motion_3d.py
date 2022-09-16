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
import types
from ..utils.converter import dict_to_json_string


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
def vertical_displacement(values={}):
    if isinstance(values['v_0y'], Symbol) and isinstance(values['angle'], Number):
        values['v_0y'] = values['v_y'] * m.sin(m.radians(values['angle']))
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
    if isinstance(values['v_0y'], Number) and isinstance(values['angle'], Number) \
            and isinstance(values['v_0'], Symbol):
        values['v_0'] = values['v_0y'] / m.sin(m.radians(values['angle']))
        if isinstance(values['v_0'], Symbol):
            values['v_0'] = values['v_x'] / m.cos(m.radians(values['angle']))
    if isinstance(values['y'], Symbol) and isinstance(values['v_0y'], Number):
        values['y'] = sqrt((values['v_y'] ** 2) / (2 * values['g']))
        if isinstance(values['y'], Symbol) and isinstance(values['v_0y'], Number):
            values['y'] = sqrt((values['v_0y'] ** 2) / (2 * values['g']))
            values['y'].subs(values)
    if isinstance(values['y'], Number) and isinstance(values['y_0'], Number) \
            and isinstance(values['v_0y'], Number) and isinstance(values['v_y'], Number) \
            and isinstance(values['t'], Symbol):
        values['t'] = (2.0 * (values['y'] - values['y_0'])) / (values['v_0y'] + values['v_y'])
        if isinstance(values['v_0y'], Number) and isinstance(values['g'], Number) \
                and isinstance(values['t'], Symbol):
            values['t'] = values['v_0y'] / values['g']
    if isinstance(values['v_y'], Symbol) and isinstance(values['t'], Number):
        values['v_y'] = values['v_0y'] - values['g'] * values['t']
    if values['counter'] < 300:
        values['counter'] += values['counter'] + 1

        return vertical_displacement(values)
    return values


##########################################################################
def horizontal_displacement(values={}):
    # print(__values)
    if isinstance(values['v_0'], Number) and isinstance(values['angle'], (Number, float)):
        values['v_x'] = values['v_0'] * m.cos(m.radians(values['angle']))
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
        values['r']= sqrt((values['x'] ** 2) + (values['y'] ** 2))
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
def time_of_flight(values={}):
    if isinstance(values['v_0'], Number):
        values['tof'] = (2 * (values['v_0'] * m.sin(values['angle']))) / values['g']
        print("\nTime of Flight:=> TOF =  ")
        values['tof'] = values['tof'].subs(values)
        pprint(values['tof'])
    if values['counter'] < 100:
        values['counter'] += values['counter'] + 1
        time_of_flight(values)
    pprint(values['y'])
    return values


##########################################################################
def trajectory(values={}):
    if not isinstance(values['v_0'], Symbol) and isinstance(values['x'], Number) \
            and isinstance(values['angle'], Number) and isinstance(values['g'], Number):
        values['y'] = (m.tan(m.radians(values['angle'])) * values['x']) - (values['g'] /
                  (2 * (values['v_0'] * m.cos(m.radians(values['angle']))) ** 2)) * (values['x'] ** 2)
    print("\nTrajectory:=> y =  ")
    if isinstance(values['y'], Symbol):
        values['y'] = values['y'].subs(values)
    pprint(values['y'])
    return values


##########################################################################
def horizontal_range(values={}):
    if not isinstance(values['R'], Symbol) and isinstance(values['v_0'], Symbol):
        values['v_0'] = sqrt((values['R'] * values['g']) / m.sin(2 * m.radians(values['angle'])))
        if isinstance(values['v_0'], Symbol):
            values['v_0'] = sqrt((values['R'] * values['g']) / m.sin(2 * m.radians(values['angle'])))
        if isinstance(values['v_0'], Number):
            values['v_0'] = round(values['v_0'], 6)
        print("Solving for v_0:")
        print('\nInitial velocity:=> v_0 =')
        pprint(values['v_0'])
    if isinstance(values['R'], Symbol) and not isinstance(values['v_0'], Symbol):
        values['R'] = ((values['v_0'] ** 2) * m.sin(2 * m.radians(values['angle']))) / values['g']
        if isinstance(values['R'], Number):
            values['R'] = round(values['R'], 6)
        print("Solving for R: ")
        print('\nRange :=> R =')
        pprint(values['R'])
    if values['counter'] < 100:
        values['counter'] += values['counter'] + 1
        return horizontal_range(values)
    values['counter'] = 1
    return values


##########################################################################
def variables_3d() -> dict:
    x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, theta = \
        symbols('x, x_0, y, y_0, z, z_0, v, v_0, v_y, v_0y, v_x, v_0x, i, j, k, t, r, g, R, tof, theta', cls=Symbol)
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

