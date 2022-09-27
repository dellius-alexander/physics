import math as m

from sympy import sqrt


#####################################################################


def get_VecX(magnitude, degrees):
    """
    Get the x-coordinates from the magnitude and direction of the vector.
    :param magnitude: magnitude of the vector
    :param degrees: degrees of the vector
    :return:
    """
    return m.fabs(magnitude) * m.cos(m.radians(degrees))


#####################################################################


def get_VecY(magnitude, degrees):
    """
    Get the x-coordinates from the magnitude and direction of the vector.
    :param magnitude: magnitude of the vector
    :param degrees: degrees of the vector
    :return:
    """
    return m.fabs(magnitude) * m.sin(m.radians(degrees))


#####################################################################


def displacement_vector(vectors=[tuple] or None, operation=None):
    """Computes the displacement vector of a list of connected vectors, given the
    magnitude and direction (degrees) of each vector.
    :param vectors: List[tuple(magnitude, direction/position/degrees)]
    :param operation: such as addition[+], subtraction[-], multiplication[*]
    :return: displacement vector(x-component,y-component)
    """
    if vectors is None:
        vectors = [tuple]
    xsum = 0
    ysum = 0
    for i, a in enumerate(vectors):
        x = get_VecX(a[0], a[1])
        y = get_VecY(a[0], a[1])
        print("index: {}".format(i))
        if operation == "+":
            print("V_r({}) = {}*i + {}*j\n".format(a[0], x, y))
            xsum += x
            ysum += y
        elif operation == "-":
            print("V_r({}) = {}*i + {}*j\n".format(a[0], x, y))
            if i == 0:
                xsum = x
                ysum = y
            else:
                xsum -= x
                ysum -= y
        elif operation == "*":
            print("V_r({}) = {}*i + {}*j\n".format(a[0], x, y))
            if i == 0:
                xsum = x
                ysum = y
            else:
                xsum *= x
                ysum *= y
    return xsum, ysum


#####################################################################


def magnitude(x, y):
    """
    Computes the magnitude or displacement vector for the vector (Vx,Vy) components.
    :param x: x-component
    :param y: y-component
    :return: the displacement vector sqrt(abs(x) ** 2 + abs(y) ** 2)
    """
    return sqrt(abs(x) ** 2 + abs(y) ** 2)


#####################################################################


def vector_angle(x, y):
    """
    Computes the vector angle given the (x,y) components.
    :param x: x-component
    :param y: y-component
    :return:  (0,180,360)
    """
    if x > 0 and y > 0:
        return m.degrees(m.atan(y / x))
    elif x < 0 and y > 0:
        return 180 + m.degrees(m.atan(y / x))
    elif x < 0 and y < 0:
        return 180 + m.degrees(m.atan(y / x))
    else:
        return 360 + m.degrees(m.atan(y / x))


#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################

if __name__ == "__main__":

    # pprint(net_displacement(10.5, 15.2))

    # Ax=5.6 Ay=-4.7

    # pprint(vector_angle(-5.6, 4.7))

    A = (5.7, 90 - 38)
    B = (4.3, 270 + 24)

    vectors = [
        # (magnitude, direction|position|degrees)
        A, B
    ]

    dv = displacement_vector(vectors, "*")
    nd = magnitude(dv[0], dv[1])
    print("DV: {}\nND: {}\n".format(dv, nd))


