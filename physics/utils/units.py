from cmath import exp
from math import floor
from sympy import symbols, init_printing

##########################################################################
##########################################################################
init_printing(pretty_printer='true')
##########################################################################
a, b, c, b, e, f, x, y, z = symbols('a,b,c,b,e,f,x,y,z')


##########################################################################
def trailing_zeros(longint):
    manipulandum = str(longint)
    manipulandum = [a for a in manipulandum]
    manipulandum_reverse = [a for a in manipulandum.__reversed__()]
    cnt_zeros = 0
    for a in manipulandum_reverse:
        if a == '0' or a == '.':
            if a == '0':
                cnt_zeros += 1
            elif a == '.':
                cnt_zeros -= 1
                continue
        elif a != '.':
            break
    return (cnt_zeros)


##########################################################################
def __geometric_mean(c, d):
    """The geometric mean  𝐺  of a pair of numbers  𝑐  and  𝑑,   𝐺(𝑐,𝑑),  
    is the square root of their product.

    - 𝐺(𝑐,𝑑)= √𝑐𝑑

Square roots violate the "keep it simple" maxim of making estimates, 
but there is an easy method for approximating the geometric mean that 
does not require taking a square root. The approximation method requires 
that the numbers be expressed in scientific notation, and is best explained 
by way of example.

Consider the range  (3×10^2,1×10^4).  To approximate the geometric mean of 
these values, first average the mantissas 3 and 1,  (1/2)(3+1)=2.  Next, 
average the exponents 2 and 4,  (1/2)(2+4)=3.  These average values become 
the mantissa and exponent of the approximate geometric mean,  2×10^3.  
When the exponents sum to an odd value, the average of the exponents is 
not an integer. In this case, round the average exponent down to the nearest 
integer, but multiply the average mantissa by 3. For example, the 
approximate geometric mean of the range  (3×10^2,1×10^5)  is  6×10^3.

    Args:
        c (int): a number
        d (int): a number
    Return: 
        (float)
    """
    # ---------------------------------------------------------------------

    # ---------------------------------------------------------------------
    num_of_trailing_zeros_L = trailing_zeros(L)
    num_of_trailing_zeros_H = trailing_zeros(H)
    mantissas_L = int(str(L).rsplit('0')[0])
    mantissas_H = int(str(H).rsplit('0')[0])
    # Consider the range  (3×10^2,1×10^4). 
    # first average the mantissas 3 and 1,  (1/2)(3+1)=2
    mantissas_avg = floor((1 / 2) * (mantissas_L + mantissas_H))
    # Next, average the exponents 2 and 4,  (1/2)(2+4)=3
    exponent_avg = (1 / 2) * (num_of_trailing_zeros_L + num_of_trailing_zeros_H)
    # These average values become the mantissa and exponent of the 
    # approximate geometric mean,  2×10^3.  When the exponents sum 
    # to an odd value, the average of the exponents is not an integer. 
    if exponent_avg % 2 != 0:
        # In this case, round the average exponent down to the nearest 
        # integer, but multiply the average mantissa by 3. For example, 
        # the approximate geometric mean of the range  (3×10^2,1×10^5)  is  6×10^3.
        mantissas_avg = mantissas_avg * exponent_avg
        exponent_avg = floor(exponent_avg)
    print('''Trailing Zeros: {0}, {1} '''.format(num_of_trailing_zeros_L, num_of_trailing_zeros_H))
    print('''Mantessa: {0}, {1} '''.format(mantissas_L, mantissas_H))
    print('Mantessa Avg: {0} '.format(mantissas_avg))
    print('Exponent Avg: {0} '.format(exponent_avg))
    # results = "{:e}".format(mantissas_avg * (10**exponent_avg))
    return mantissas_avg * (10 ** exponent_avg)


##########################################################################
# if __name__ == "__main__":
#     # print(trailing_zeros(109000))
#     # exit(0)
#     # L = 3 * 10**2
#     # H = 1 * 10**4
#     L = 100 * 10 ** 4
#     H = 109 * 10 ** 4
#     print(__geometric_mean(L, H))
