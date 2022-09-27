from sympy import symbols, init_printing, pretty_print, Integral, \
    sin, cos, tan, cot, sec, csc, pretty

init_printing(pretty_printer='true')

#####################################################################
#####################################################################
#      Work Done by a Force
#####################################################################
"""
In physics, work is related to force, like a push or pull on an object. 
When a force moves an object, we say the force does work on the object. 
In this sense, work can be thought of as the amount of energy it takes 
to move an object. According to physics, when we have a constant force, 
work can be expressed as the product of force and distance.

In the English system, the unit of force is the pound and the unit of 
distance is the foot, so work is given in foot-pounds. In the metric 
system, kilograms and meters are used. One newton ( N ) is the force 
needed to accelerate 1kg of mass at the rate of 1m/sec2. Thus, the most 
common unit of work is the newton-meter. This same unit is also called 
the joule. Both are defined as kilograms times meters squared over 
seconds squared (1 N = 1 * kg⋅m^2 / s^2).

When we have a constant force, things are pretty easy: If a constant 
force F moves an object by d units, the work done is W = F * d.

Suppose we have a variable force F(x) that moves an object in a positive 
direction along the x-axis from point a to point b. To calculate the 
work done, we partition the interval [a, b] and estimate the work done 
over each sub-interval. So, for i=0,1,2,…,n, let P={x_i} be a regular 
partition of the interval [a,b], and for i=1,2,…,n, choose an arbitrary 
point x_i ∈ [x_i−1,x_i]. To calculate the work done to move an object from 
point x_i−1 to point x_i, we assume the force is roughly constant over the 
interval, and use F(x_i) to approximate the force. The work done over the 
interval [xi−1, x_i], then, is given by:

- W_i ≈ F(x_i) * (x_i − x_i−1)
-     = F(x_i) Δx.

Therefore, the work done over the interval [a,b] is approximately:

- W = [ n ∑ i_1 ] W_i
-   ≈ [ n ∑ i_1 ] F(x_i) Δx.

Taking the limit of this expression as n→∞ gives us the exact value for work:

- W = [ lim n→∞ ∑ i_1 ] F(x_i) Δx 
-   = ∫ [a, b] F(x)dx.

Thus, we can define work as follows.

Definition:

If a variable force F(x) moves an object in a positive direction along the 
x-axis from point a to point b, then the work done on the object is:

- W = ∫ [a, b] F(x)dx.

Note that if F is constant, the integral evaluates to:
 
- F * (b−a) = F * d, 

which is the formula we stated at the beginning of this section.

Mass–Density Formula of a Circular Object:

Let ρ(x) be an integrable function representing the radial density of a
disk of radius r. Then the mass of the disk is given by:

- m = ∫ [0, r] 2π * x * ρ(x) dx.

"""


#####################################################################
#      Work Done by Constant Force 1
#####################################################################
def _constant_force_(weight, displacement) -> object:
    """Work done by constant force:

    The formula for work done by a constant force is:

    -  W = F * d,

    where F is the magnitude of the force and d is the displacement.
    A Joule is defined as:

    - 1J = 1Nm (Nm = newton-meter).


    :param weight:
    :param displacement:
    :return:
    """
    _w_ = weight
    _d_ = displacement
    _work_ = _w_ * _d_
    print("\nW = {0} * {1}".format(_w_, _d_))
    print("\nW = {0} Joule".format(_work_))
    return _work_


#####################################################################
#      Work Done by Variable Force 2
#####################################################################
def _variable_force_(fx, lower_bound, upper_bound, variable_of_integration) -> object:
    """Work Done by Variable Force:

    we need to recall the mass-density formula of a one-dimensional object,
    as well as how to calculate the work done on an object by a variable force.

    Linear density of the string is equal to the mass divided by the length
    of the string:

    - p = m/L, where m is mass and L is length of the object.

    As the string is wound up, the portion of the cable that is hanging down
    decreases. The mass of the cable alone can therefore be expressed as
    the linear density multiplied by x, the length of the hanging portion
    of the cable. Since we also know that F=ma and the acceleration is equal
    to g, the force from the cable alone is equal to:

    - F(x) = ρxg

    The force from the weight of the crate is equal to its mass multiplied
    by g. The total force is therefore:

    - F(x) = pxg + pL

    The mass m of a one-dimensional object oriented along the x-axis over the
    interval [a,b] is given by:

    - m = ∫ [a, b] ρ(x) dx,

    where ρ(x) is the linear density of the object at a point x in the interval.
    When linear density is constant, this simplifies to:

    - m = ∫ [a, b] ρ dx.

    If a variable force F(x) moves an object in a positive direction along the
    x-axis from point a to point b, then the work done on the object is:

    - W = ∫ [a, b] F(x) dx.

    :param fx:
    :param lower_bound:
    :param upper_bound:
    :param variable_of_integration:
    :return:
    """
    _l_ = lower_bound
    _u_ = upper_bound
    _var_ = variable_of_integration
    _work_ = Integral(fx, (_var_, _l_, _u_))
    _work_sol_ = _work_.doit()
    print("\nWork Integral: \n")
    pretty_print(_work_)
    print("\nWork = \n")
    pretty_print(_work_sol_)
    return _work_sol_


#####################################################################
#      Work Done by Variable Force 2
#####################################################################
def variable_force(mass_of_object, displacement_of_object, mass_of_string,
                   length_of_string, acceleration, additional_length) -> object:
    """Work Done by Variable Force:

    we need to recall the mass-density formula of a one-dimensional object,
    as well as how to calculate the work done on an object by a variable force.

    Linear density of the string is equal to the mass divided by the length
    of the string:

    - p = m/L, where m is mass and L is length of the object.

    As the string is wound up, the portion of the cable that is hanging down
    decreases. The mass of the cable alone can therefore be expressed as
    the linear density multiplied by x, the length of the hanging portion
    of the cable. Since we also know that F=ma and the acceleration is equal
    to g, the force from the cable alone is equal to:

    - F(x) = ρxg

    The force from the weight of the crate is equal to its mass multiplied
    by g. The total force is therefore:

    - F(x) = pxg + pL

    The mass m of a one-dimensional object oriented along the x-axis over the
    interval [a,b] is given by:

    - m = ∫ [a, b] ρ(x) dx,

    where ρ(x) is the linear density of the object at a point x in the interval.
    When linear density is constant, this simplifies to:

    - m = ∫ [a, b] ρ dx.

    If a variable force F(x) moves an object in a positive direction along the
    x-axis from point a to point b, then the work done on the object is:

    - W = ∫ [a, b] F(x) dx.

    :param mass_of_object:
    :param displacement_of_object:
    :param mass_of_string:
    :param length_of_string:
    :param acceleration:
    :param additional_length:
    :return:
    """
    x = symbols('x')
    p_string = mass_of_string / length_of_string
    if additional_length is not None:
        fx = p_string * (x + additional_length) * acceleration + (mass_of_object * acceleration)
    elif additional_length is None and mass_of_object is not None:
        fx = p_string * x * acceleration + (mass_of_object * acceleration)
    else:
        fx = p_string * x * acceleration
        displacement_of_object = length_of_string
    _fx_int_ = Integral(fx, (x, 0, displacement_of_object))
    _fx_int_sol_ = _fx_int_.doit()
    print("\nWork required : \n")
    pretty_print(_fx_int_)
    print("\nSolution: \n")
    pretty_print(_fx_int_sol_)

    #####################################################################
    #####################################################################
    #                           Main Method
    #####################################################################


if __name__ == "__main__":
    # main method
    x, y, t, e = symbols('x, y, t, e')
    _weight_ = 1  # N
    _displacement_ = 9.8  # m
    # p = m/L
    object_mass = 44
    object_displacement = 2
    string_mass = 12
    string_length = 2
    add_length = None
    accel = 9.8
    f = 21 * x ** 2 + 3
    a = 5
    b = 7
    variable = x
    # _constant_force_(_weight_, _displacement_)
    variable_force(object_mass, object_displacement, string_mass, string_length, accel, add_length)
