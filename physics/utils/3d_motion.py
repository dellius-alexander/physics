from sympy import init_printing, symbols, sin, cos, tan, atan, sqrt, integrals, \
    Function, Number, pprint, solve, init_session, printing, Symbol, NumberSymbol
import re
import mpmath as m
###########################################################
init_printing(use_unicode=True)
###########################################################
# GLOBAL Symbols
x, y, z, t, i, k, j, v, a, b, c, m, s, y_0, x_0, v_0y, v_0x, v_y, v_x, d  = \
    symbols('x, y, z, t, i, k, j, v, a, b, c, m, s, y_0, x_0, v_0y, v_0x, v_y, v_x, d', cls=Symbol)

f, g, h =  symbols('f, g, h', cls=Function)
###########################################################
def acceleration_vector(func=Function, sym=symbols, time=Number):
    derivative = func.diff(sym)
    direction = derivative.subs(sym, time)
    magnitude = magnitude_func(direction,2)
    print("\nAcceleration Vector: ", end=None)
    pprint(derivative)
    print("\nMagnitude of Acceleration: ")
    print(magnitude)

###########################################################
def magnitude_func(func=Function or list, p=Number):
    fk = []
    if not isinstance(func, (list)):
        for n in func.__str__().split():
            if re.compile(r'^[0-9]*[.]{0,1}[0-9]*$').match(n) :
                fk.append(n)
            elif re.compile(r'^([0-9.]*[*]{0,1}[a-zA-Z]{0,1})$').match(n) :
                for a in n.split('*'):
                    if re.compile(r'^[0-9]*[.]{1}[0-9]*$').match(a) and a != " ":
                        fk.append(f"{a}**{p}")
                    else:
                        fk.append(a)
            else:
                fk.append(n)
    magnitude = 0.0
    for a in fk:
        if not a.isalpha() and not re.compile(r'(\+|-/)').match(a):
            a = eval(a)
            # print(a)
            magnitude += a
    magnitude = abs(sqrt(magnitude))
    return magnitude

###########################################################
def formulas():
    #######################################################
    # Vertical velocity due to gravity:
    f = v_0y - v_y - g * t
    pprint(solve(f, t))
    print("\n")
    #######################################################
    # Projectile Motion
    print("Projectile Motion")
    print("f = \n")
    f = v_0x * t + (1 / 2) * g * t ** 2
    pprint(solve(f, t))
    print("\nf = \n")
    f = y_0 - y + v_0y * t - (1 / 2) * g * t ** 2
    pprint(solve(f, y_0))
    print("\nf = \n")
    f = v_0y - v_y - g * t
    pprint(solve(f, t))
    print("\nf = \n")
    f = x_0 + v_0x * t - x
    pprint(solve(f, v_0x))
    print("\n")

###########################################################
if __name__ == '__main__':
    f = 5.0 * t * i + 2.0 * t ** 2 * j - 2.0 * t ** 3 * k
    acceleration_vector(f, t, 2.0)
    #######################################################

