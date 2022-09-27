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

from typing import List, Set, Dict, Tuple, Optional, Any, NamedTuple, Mapping
import json
import math as m
import sys
from pandas.io.formats import string
from sympy import init_printing, Number, Symbol, Function

init_printing(pretty_print=True)


#####################################################################


class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.f(*args)
        # Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]


#####################################################################


def scale_to(value, _from, _to):
    """Convert value from one unit to another unit.
    :param value: value to be converted
    :param _from: tuple(value,metric unit)
    :param _to: tuple(value,metric unit)
    :return: string
    """
    return "{0} {1}".format((value * _to[0]) / _from[0], _to[1])


#####################################################################


def rad_to_deg(value):
    """
    Radians  × (180/π) = Degrees
    1rad × 180/π = 57.296°
    :param value: radians
    :return: value in degrees
    """
    return (value * 180) / m.pi


#####################################################################


def deg_to_rad(value):
    """
    Degrees x (π/180) = Radians
    360 Degrees = 2π Radians
    180 Degrees = π Radians
    :param value: degrees
    :return: value in radians
    """
    return value * (m.pi / 180)


#####################################################################

@Memoize
def base_log10(num):
    """
    Calculates the base-10 logarithm.

    Formula:
    Log base 10 of a number "x" is the power to which the number 10 must
    be raised to obtain the value x.
    Hence, log10 calculation can be done using the formula,
    Log10 n = 10^x = n
    Where,
    x is the log10 of n.
    That is, x the number of times number 10 should be multiplied by itself to obtain n.
    :param num: number
    :return: x = the number of times number 10 should be multiplied by itself to obtain n.
    """
    return m.log10(num)


#####################################################################


def scientific_notation(num):
    """
    Converts the number into scientific notation of the number.
    :param num: the number to convert
    :return: Return scientific notation of the number
    """
    new_num = ""
    for i, n in enumerate(iter(str(num))):
        if i == 0:
            new_num += n
        elif i == 1:
            new_num += "." + n
        else:
            new_num += n
    ans = base_log10(num)
    print(f"{0} X 10^{1}".format(new_num, round(ans)))


#####################################################################
def dict_to_json_string(dict_map: Dict[Mapping, List[str]] = None) -> Tuple[str, Dict]:
    # try:
    json_dict = {}
    print(type(dict_map))
    __json = str
    __json = lambda __json_string__: json.dumps(__json_string__,
                                                skipkeys=False,
                                                ensure_ascii=True,
                                                check_circular=True,
                                                allow_nan=True,
                                                cls=json.JSONEncoder,
                                                indent=4,
                                                separators=(',', ':'),
                                                sort_keys=True,
                                                default=Function)
    if isinstance(dict_map, dict):
        for k, v in zip(dict_map.keys(), dict_map.values()):
            # print(k, v)
            arr_list = []
            if isinstance(v, list):

                for n, i in enumerate(v):
                    # print(n, i)
                    arr_list.append(str(i))
                json_dict[f'{k}'] = arr_list
            else:
                json_dict[f'{k}'] = [str(v)]
        return __json(json_dict)
    elif isinstance(dict_map, dict):
        for k, v in zip(dict_map.keys(), dict_map.values()):
            print(k, v)
    elif isinstance(dict_map, list):
        for n, i in enumerate(dict_map):
            # print(n, i)
            json_dict[f'{i}'] = [str(i)]
            return __json(json_dict)
    else:
        return dict_map


#####################################################################
