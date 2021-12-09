import matplotlib as plt
import turtle
import time

def fwd(t, dist, points):
    t.forward(dist)
    points.append(tuple(t.pos()))


def hilbert(n, size):
    t = turtle.Turtle()
    t.penup()
    t.goto(-size / 2.0, size / 2.0)
    t.pendown()
    points = recurse(t, n, -1, size/(2**n - 1), [tuple(t.pos())])
    return points

def recurse(t, n, dirc, dist, points):
    if n == 0:
        return points
    t.left(90 * dirc)
    recurse(t, n-1, -dirc, dist, points)
    fwd(t, dist, points)
    t.right(90 * dirc)
    recurse(t, n-1, dirc, dist, points)
    fwd(t, dist, points)
    recurse(t, n-1, dirc, dist, points)
    t.right(90 * dirc)
    fwd(t, dist, points)
    recurse(t, n-1, -dirc, dist, points)
    t.left(90 * dirc)
    return points

def plot():
    s = turtle.getscreen()


if __name__ == "__main__":
    points = hilbert(4, 300)
    print(points)