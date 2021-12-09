'''
source: https://github.com/SankarMridha/Moore-Curve/blob/master/MoCurve.m
'''

axiom = "LFL+F+LFL"
rules = {"L":"+RF+LFL+FR-",
         "R":"+LF-RFR-FL+", 
         "+":"+", 
         "-":"-",
         "F":"F"}

class Point():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def generate_lsys(n, rule, depth):
    '''
    Generate the Lindenmayer pattern

    n = desired degree of the pattern
    rule = Lindenmayer string rule
    depth = current degree of depth into the pattern
    '''
    # if desired depth achieved, return rule
    if depth == n:
        return rule
    
    # go through current rule to generate next depth rule
    new_rule = ""
    for var in rule:
        new_rule += (rules[var])

    return generate_lsys(n, new_rule, depth+1)


def lsys_to_coord(rule, startx, starty):
    '''
    Convert Lindenmayer string rule into points
    '''
    start = Point(startx, starty)
    points = [start]
    direction = 1

    # 4 directions: 1 for Up, 2 for Left, 3 for Down, 4 for Right 
    px, py = startx, starty
    for letter in rule:
        # L and R is only used for recursive rule construction
        if letter == 'L' or letter == 'R':  
            continue
        
        # rotate direction
        elif letter == '-':
            direction += 1
        elif letter == '+':
            direction -= 1

        # check if direction is valid
        if direction < 1:
            direction = 4
        if direction > 4:
            direction %= 4

        # move forward
        elif letter == 'F':
            if direction == 1:
                py += 1
            elif direction == 2:
                px += 1
            elif direction == 3:
                py -= 1
            elif direction == 4:
                px -= 1
            print(px, py)
            points.append(Point(px, py))

    return points

def print_points(points):
    for point in points:
        print(point.x, point.y)
        print()

# check lsys generation
rule = generate_lsys(1, axiom, 0)
# print(rule)

# check lsys to coordinate conversion
points = lsys_to_coord(rule, 0, 0)

print_points(points)