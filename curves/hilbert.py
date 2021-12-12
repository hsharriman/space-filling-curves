import matplotlib as plt
import turtle
import time

def fwd(t, dist, points):
    """
    Move turtle forward and add new position to list

    :param t: turtle.Turtle instance
    :param dist: int, distance for turtle to move forward
    :param points: [tuple], current list of (x,y) coordinates
    :returns: None
    """
    t.forward(dist)
    points.append(tuple(t.pos()))


def hilbert(n, size):
    """
    Create a Hilbert curve using turtle graphics

    :param n: int, recursion depth for Hilbert curve
    :param size: int, scalar for unit square that Hilbert curve is contained in
    :returns: list of (x,y) coords corresponding to all points the turtle has visited
    """
    t = turtle.Turtle()
    t.penup()
    t.goto(-size / 2.0, size / 2.0)
    t.pendown()
    points = recurse(t, n, -1, size/(2**n - 1), [tuple(t.pos())])
    return points

def recurse(t, n, dirc, dist, points):
    """
    Recursive function for Hilbert Curve

    :param t: turtle.Turtle instance
    :param n: int, current recursion depth
    :param dirc: int, direction to turn (1 or -1)
    :param dist: int, distance for turtle to travel forwards
    :param points: [tuple], array of (x,y) coordinates of turtle's position
    :returns: [tuple], current list of points
    """
    if n == 0:
        return points

    #turn turtle 90 deg left. if deg =-1 then it will turn right instead
    t.left(90 * dirc)  
    recurse(t, n-1, -dirc, dist, points)

    #move turtle forward after completing recurse() call
    fwd(t, dist, points)
    t.right(90 * dirc)
    recurse(t, n-1, dirc, dist, points)

    fwd(t, dist, points)
    recurse(t, n-1, dirc, dist, points)

    t.right(90 * dirc)
    fwd(t, dist, points)
    recurse(t, n-1, -dirc, dist, points)

    #need to turn turtle left after completing iteration
    t.left(90 * dirc)
    return points


if __name__ == "__main__":
    points = hilbert(4, 300)
    print(points)