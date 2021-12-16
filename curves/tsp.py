import numpy as np
import math
import time
import sys

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def find_distance(p1, p2):
    return math.sqrt(abs(p1.x - p2.x)**2 + abs(p1.y - p2.y)**2)

def setup(n, map_n):
    '''
    1. Generate distance matrix for specified dimension
    2. Generate random points for specified number of points
    3. Fill in distance matrix 

    n: the number of points to be generated
    map_n: dimension of the grid
    '''

    # make map based on dimension
    points = {}
    matrix = np.zeros(shape=(n,n))

    # generate random points
    for i in range(n):
        px, py = np.random.randint(0, map_n + 1), np.random.randint(0, map_n + 1)
        points[i] = Point(px, py)

    # build weight between points (right now, the weight is purely the distance)
    for i in range(len(points)):
        for j in range(len(points)):
            if i == j:
                continue
            matrix[i][j] = find_distance(points[i], points[j])
    
    return points, matrix

def tsp(P, D):
    '''
    Finds the shortest route that goes through all the given points.

    P: a mapping of unique id numbers to Point objects
    D: a distance matrix between all possible combinations of two points
    '''
    n, n = D.shape
    points = np.arange(0, n)
    
    # init min_dist for recording all possible routes
    min_route = []
    min_dist = sys.maxsize

    for i in range(n):
        # initialize hashmap of visited status
        visited = {}
        for p in range(n):
            visited[p] = False

        # initialize list and total_dist to keep track of route and total distance
        route = []
        total_dist = 0

        # start at first point from points & mark it visited
        route.append(points[i])
        visited[points[i]] = True

        # find the closest point each iteration and run until all the points are visited
        # while False not in visited.values():
        while len(route) != len(points):
            closest_dist = sys.maxsize
            closest_point = None

            # find the closest point
            for j in range(n):
                # case when at D[i,i]
                if route[-1] == [j]:
                    continue
                
                # case when unvisited, closer distance point is found
                if D[route[-1]][j] < closest_dist and visited[j] == False:
                    closest_dist = D[route[-1]][j] 
                    closest_point = j

            # add closest_dist to total_dist, add closest point to route, and mark it visited
            total_dist += closest_dist
            route.append(closest_point)
            visited[closest_point] = True

        # print('closest: ', closest_dist)
        # print('route: ', route)

        # add the distance between the last point and the first point
        total_dist += D[route[-1]][route[0]]
    
        if total_dist <= min_dist:
            min_dist = total_dist
            min_route = route

    # convert route to coord points
    for i in range(len(min_route)):
        coord = P[min_route[i]]
        min_route[i] = coord

    # return the total distance required for the route and the route
    return min_dist, min_route

def get_runtime_tsp(P, D):
    ''' 
    Returns the total runtime of the traveling_salesman() algorithm
    D: a distance matrix between all possible combinations of two points
    '''
    start_time = time.time()
    tsp(P, D)

    return time.time() - start_time

def print_points(points):
    for point in points:
        print(point.x, point.y)
        print()

def dict_to_coords(points):
    coords = []
    for i in range(len(points)):
        coords.append((points[i].x, points[i].y))
    return coords

def list_to_coords(points):
    coords = []
    for p in points:
        coords.append((p.x, p.y))
    return coords

P, D = setup(5, 30) # generate 5 points in a 30x30 grid
total_dist, route = tsp(P, D)
# print(list_to_coords(route))