import sys

def min_dist(n, points):

    points = zip(points[0::1], points[1::2])
    return n, len(points)



if __name__ == "__main__":

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    points = data[1:]

    print(min_dist(n, points))
