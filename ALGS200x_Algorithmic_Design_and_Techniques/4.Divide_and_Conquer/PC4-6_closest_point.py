import sys
import math

def euclidean(a, b):
    """compute euclidean distance between two points
    (tuples with x and y as elements)"""

    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def sort_X(points):
    """sort list of points according to x coordinate"""

    n = len(points)//2
    A = [(points[2*i], points[2*i + 1]) for i in range(n)]
    Ax = sorted(A, key = lambda x: x[0])
    return Ax

def sort_Y(points):
    """sort list of points according to x coordinate"""

    n = len(points)//2
    A = [(points[2*i], points[2*i + 1]) for i in range(n)]
    Ay = sorted(A, key = lambda x: x[1])
    return Ay

def filter_strip(points, m, d):
    """filter a list o points based on their x coordinate
    to be included between (m - d) and (m - d)"""

    strip = []
    for point in points:
        if abs(point[0] - m) < d:
            strip.append(point)
    return strip

def find_min_dist(Ax):
    """find the minimum distance between a set of points"""

    n = len(Ax)//2
    lhs, rhs = Ax[:n], Ax[n:]

    if len(Ax) <= 3: return euclidean(Ax[0], Ax[1])
    else:
        leftSet_minDist = find_min_dist( lhs )
        rightSet_minDist = find_min_dist( rhs )

    d = min(leftSet_minDist, rightSet_minDist)
    median = (lhs[-1][0] + rhs[0][0]) / 2

    strip = sort_Y(filter_strip(Ax, median, d))

    # need to check just the 6
    for i in range(len(strip)):
        js = min(len(strip), i + 7)
        for j in range(i + 1, js):
            ds = euclidean(strip[i][0], strip[j][0])
            if ds < d: d = ds

    return round(d)


if __name__ == "__main__":

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    points = data[1:]

    sorted_points = sort_X(points)
    print(find_min_dist(sorted_points))
