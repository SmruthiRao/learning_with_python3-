import math


def distance(x1, y1, x2, y2):
    # dx = x2 - x1
    # dy = y2 - y1
    # dist_squared = dx ** 2 + dy ** 2
    # dist = dist_squared ** 0.5
    # return dist
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


def area(rad):
    return 3.14 * rad * rad


# print(distance(0, 0, 4, 5))
r = distance(0, 0, 4, 4)
print('area of circle : ', area(r))
