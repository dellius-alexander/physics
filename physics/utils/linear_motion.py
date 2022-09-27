import math as m
from sympy import Function, symbols, simplify, Number, \
    pretty_print, init_printing, solve
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
init_printing(pretty_print=True)


#####################################################################

def displacement(x_0, x_f):
    """
    Displacement is the change in position of an object:

    - Δx = x_f - x_0

    - where Δx is displacement, x_f is the final position, and x_0 is the initial position.

    We use the uppercase Greek letter delta (Δ) to mean “change in”
    whatever quantity follows it; thus, means change in position
    (final position less initial position). Solve for displacement by
    subtracting initial position x_0 from final position x_f .

    :param x_0: initial position
    :param x_f: final position
    :return: Δx is the displacement
    """
    return x_f - x_0


#####################################################################

def total_displacement(values=[]) -> dict:
    """
    ∑ ∆x¡ = n¡ + ... + n_n = total displacement

    :param values: list of displacements
    :return: {"total_displacement": value, "total_distance": value}
    """
    total_disp = 0
    total_dist = 0
    for n in values:
        total_disp += n
        total_dist += abs(n)
    return {"total_displacement": total_disp, "total_distance": total_dist}


#####################################################################

def avg_velocity(distances=[], times=[], metrics={}) -> dict:
    """
    Average Velocity = (Total displacement) / (Elapsed Time)

    :param distances: list of displacements
    :param times: list of times
    :param metrics: dict: {"unit": value, "time": value}
    :return: {"average_velocity": value,
                    "total_displacement": value,
                    "total_displacement_magnitude": value,
                    "total_distance": value}
    """
    vel_vectors = []
    # step 1: find the total displacement
    if len(distances) >= 2:
        for i, k in enumerate(zip(distances, times)):
            # print(i, k)
            if k is not None and i < len(distances) - 1:
                dd = displacement(k[0], distances.__getitem__(i + 1))
                td = displacement(k[1], times.__getitem__(i + 1))
                vel_vectors.append({f"displacement": dd,
                                    f"interval": td})
    displacements = [f"{a['displacement']} {metrics['unit']}/{metrics['time']} @ " \
                     f"{a['interval']} {metrics['time']}" for a in vel_vectors]
    print("Displacement intervals: {}".format(displacements))
    totals = displacement([a['displacement'] for a in vel_vectors])
    avgv = totals['total_displacement'] / max(times)
    # print("Total displacement: {}".format(total_disc))
    # print("Average Velocity: {}".format(avgv))
    # print("Total Distance Traveled: {}".format(total_dist))
    # Graph Position vs Time
    plot_graph(
        times,
        distances,
        "Position vs Time",
        f"Time ({metrics['time']})",
        f"Position ({metrics['unit']})"
    )
    # Graph Velocity vs Time
    plot_graph(
        [a['interval'] for a in vel_vectors],
        [a['displacement'] for a in vel_vectors],
        "Velocity vs Time",
        f"Time ({metrics['time']})",
        f"Velocity ({metrics['unit']})"
    )
    return {"average_velocity": f"{avgv} {metrics['unit']}/{metrics['time']}",
            "total_displacement": f"{totals['total_displacement']} {metrics['unit']}",
            "total_displacement_magnitude": f"{abs(totals['total_displacement'])} {metrics['unit']}",
            "total_distance": f"{totals['total_distance']} {metrics['unit']}"}


#####################################################################

def avg_velocity_intervals(distances=[], times=[], metrics={}):
    """
       The instantaneous velocity of an object is the limit of the
       average velocity as the elapsed time approaches zero, or the
       derivative of x with respect to t:

       - v(t) = (d/dt) * x(t)
       - Average Velocity = (Total displacement) / (Elapsed Time)

       :param distances: list of displacements
       :param times: list of times
       :param metrics: dict: {"unit": value, "time": value}
       :return: {"average_velocity": value,
                       "total_displacement": value,
                       "total_displacement_magnitude": value,
                       "total_distance": value}
       """
    vel_vectors = []
    # find the velocity during each time interval by taking the slope of the line using the grid
    if len(distances) >= 2:
        for i, k in enumerate(zip(distances, times)):
            # print(i, k)
            if k is not None and i < len(distances) - 1:
                dd = displacement(k[0], distances.__getitem__(i + 1))
                td = displacement(k[1], times.__getitem__(i + 1))
                vel_vectors.append({f"velocity": dd / td,
                                    f"interval": td})
    velocity_vectors = [f"{a['velocity']} {metrics['unit']}/{metrics['time']} @ " \
                        f"{a['interval']} {metrics['time']}" for a in vel_vectors]
    print("Velocity Vectors: {}".format(velocity_vectors))
    totals = displacement(distances)
    avgv = totals['total_displacement'] / max(times)
    # print("Total displacement: {}".format(total_disc))
    # print("Average Velocity: {}".format(avgv))
    # print("Total Distance Traveled: {}".format(total_dist))
    # Graph Position vs Time
    plot_graph(
        times,
        distances,
        "Position vs Time",
        f"Time ({metrics['time']})",
        f"Position ({metrics['unit']})"
    )
    # Graph Velocity vs Time
    plot_graph(
        [times.__getitem__(i) for i in range(1, len(times))],
        [a['velocity'] for a in vel_vectors],
        "Velocity vs Time",
        f"Time Interval ({metrics['time']})",
        f"Velocity ({metrics['unit']})"
    )
    return {"average_velocity": f"{avgv} {metrics['unit']}/{metrics['time']}",
            "total_displacement": f"{totals['total_displacement']} {metrics['unit']}",
            "total_displacement_magnitude": f"{abs(totals['total_displacement'])} {metrics['unit']}",
            "total_distance": f"{totals['total_distance']} {metrics['unit']}"
            }


#####################################################################

def plot_graph(x, y, title, xlabel, ylabel):
    """
    Plots a graph with gridlines.
    :param x: time
    :param y: distance/velocity/acceleration, etc...
    :param title: graph title
    :param xlabel: x-label
    :param ylabel: y-label
    :return:
    """
    data = {'distance': y,
            'time': x}
    fig = plt.figure(1)
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.legend(loc='upper left')
    # set the x and y limits/bounds
    # plt.xlim(min(data['time']) - 0.1, max(data['time']) + 0.1)
    plt.xlim()
    # plt.ylim(min(data['distance']) - 0.1, max(data['distance']) + 0.1)
    plt.ylim()

    plt.grid()
    plt.plot(data['time'], data['distance'], 'r', label=f"y={y}")
    plt.title(title)
    plt.show()


#####################################################################

def average_speed(distances=[], times=[], metrics={}):
    """
    calculate the average speed by finding the total distance traveled divided by the elapsed time.
    :param distances: list of displacement values
    :param times: list of timestamps
    :param metrics: {units: units of measurement, time}
    :return:
    """
    avg_speed = sum(distances) / sum(times)
    return f"{avg_speed} {metrics['unit']}/{metrics['time']}"


#####################################################################


def instantaneous_velocity(var=symbols, vsub=Number, func=Function, metrics={}):
    diff = func.diff(var)
    ans = diff.subs(var, vsub)
    pretty_print(func)
    pretty_print(diff)
    return ans


#####################################################################


def velocity(var=symbols, vsub=Number, func=Function):
    """

    :param var:
    :param vsub:
    :param func:
    :return:
    """
    return func.subs(var, vsub)


#####################################################################


def speed(instantaneous_velocity_value):
    """
    Speed = |v(t)|
    :param instantaneous_velocity_value:
    :return: |v(t)|
    """
    return abs(instantaneous_velocity_value)


#####################################################################


def free_fall(
        initial_velocity=None,
        final_velocity=None,
        initial_displacement=None,
        final_displacement=None,
        time_traveled=None,
        gravity=9.8):
    """
    We assume here that acceleration equals −g (with the positive direction upward).

    :param initial_velocity: initial velocity
    :param final_velocity: final velocity
    :param initial_displacement: initial displacement
    :param final_displacement: final displacement
    :param time_traveled: travel time t
    :param gravity: gravity: +9.8 m/s^2 direction -upward and +downward OR -9.8 m/s^2 direction +upward and -downward
    :return: depending on values provided: v_f = v_i - gt or y_f = y_i + v_it - 1/2 gt^2 or
    v_f^2 = v_i^2 - 2g (y_f - y_i)
    """
    v_i, v_f, y_i, y_f, t, g, y = symbols('v_i, v_f, y_i, y_f, t, g, y')

    if initial_velocity is not None and \
            time_traveled is not None or time_traveled is None and \
            final_displacement is None:
        # solve for v_f = v_i - g * t
        if time_traveled is not None and final_velocity is None:
            v_i = initial_velocity
            g = gravity
            t = time_traveled
            y = v_i - g * t
            pretty_print(y)
            return y
        # solve for time_traveled
        elif time_traveled is None and final_velocity is not None and final_displacement is not None:
            v_i = initial_velocity
            v_f = final_velocity
            g = gravity
            y = v_i - g * t
            y = solve(y, t) - v_f
            pretty_print(y)
            return y
    if initial_velocity is not None or initial_velocity is None and time_traveled is not None and initial_displacement is not None:
        # solve for y_f = y_i + v_i * t - 1/2 gt^2
        y = y_i + v_i * t - 1/2 * g * t**2
        pretty_print(y)
        if initial_velocity is not None and final_displacement is None:
            return initial_displacement + (initial_velocity * time_traveled) - (1 / 2 * (gravity * (time_traveled ** 2)))
        elif initial_velocity is None and final_displacement is not None:
            y_i = initial_displacement
            y_f = final_displacement
            t = time_traveled
            g = gravity
            y = y_i - y_f + v_i * t - 1 / 2 * g * t ** 2
            y = solve(y, v_i)
            return y
    if initial_velocity is not None and \
            initial_displacement is not None and time_traveled is None:
        # solve for v_f^2 = v_i^2 - 2g (y_f - y_i)
        if final_velocity is None and final_displacement is not None and initial_displacement is not None:
            v_i = initial_velocity
            g = gravity
            y_i = initial_displacement
            y_f = final_displacement
            y = m.sqrt(v_i**2 - 2 * g * (y_f - y_i))
            pretty_print(y)
            return y
        elif final_displacement is None and final_velocity is not None:
            v_i = initial_velocity
            v_f = final_velocity
            g = gravity
            y_i = initial_displacement
            y = m.sqrt(v_i ** 2 - 2 * g * (y_f - y_i))
            y = solve(y, y_f) - v_f
            pretty_print(y)
            return y
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
#####################################################################


if __name__ == '__main__':
    x, y, z, t = symbols('x, y, z, t')

    #################################################################
    print(free_fall(
            initial_displacement=0,
            initial_velocity=24.5,
            final_velocity=0,
            gravity=9.8))

    #################################################################
    # data = {
    #     "time": [a for a in range(0, 5)],
    #     "y(m)": [free_fall(
    #         initial_velocity=-4.9,
    #         initial_displacement=0,
    #         gravity=9.8,
    #         time_traveled=a) for a in range(0, 5)],
    #     "v(m/s)": [free_fall(
    #         time_traveled=a,
    #         initial_velocity=-4.9,
    #         gravity=9.8) for a in range(0, 5)]
    # }
    # df = pd.DataFrame(data=data).set_index('time')
    # pretty_print(df)
    #################################################################
    # dist = [0, 0.5, 0.5, 0]
    # time = [0, 0.5, 1.0, 2.0]
    # metric = {"unit": "km", "time": "s"}
    # print(average_speed(distances=dist, times=time, metrics=metric))
    # print(avg_velocity_intervals(dist, time, {"unit": "km", "time": "s"}))
    # dist = [0, 0.5, 0, 1.0, (-0.75)]
    # time = [0, 9, 18, 33, 58]
    # print(avg_velocity(dist, time, {"unit": "km", "time": "s"}))
    # plot_graph(time, dist)
    # print([time.__getitem__(i) for i in range(1, len(time))])
    # f = 3.0 * t - 3.0 * t ** 2
    # time = [0.25, 0.5, 1.0]
    # metric = {"unit": "m", "time": "s"}
    # plot_graph(
    #     time,
    #     [f.subs(t, a) for a in time],
    #     "Position vs Time",
    #     f"Time Interval ({metric['time']})",
    #     f"Velocity ({metric['unit']})"
    # )
    # d = f.diff(t)
    # plot_graph(
    #     time,
    #     [d.subs(t, a) for a in time],
    #     "Velocity vs Time",
    #     f"Time Interval ({metric['time']})",
    #     f"Velocity ({metric['unit']})"
    # )
    # inst_vel = 0
    # inst_vel = [instantaneous_velocity(t, a, f, metric) for a in time]
    # print(inst_vel)
    # plot_graph(
    #     time,
    #     [abs(a) for a in inst_vel],
    #     "Speed vs Time",
    #     f"Time Interval ({metric['time']})",
    #     f"Velocity ({metric['unit']})"
    # )
    # print(average_speed(inst_vel, time, metric))
    # # print(velocity(t, 1.0, f), "m/s")
    # # print(velocity(t, 3.0, f), "m/s")
    # ans1 = (velocity(t, 3.0, f) - velocity(t, 1.0, f)) / displacement(1.0, 3.0)
    # print(ans1, "m/s")
