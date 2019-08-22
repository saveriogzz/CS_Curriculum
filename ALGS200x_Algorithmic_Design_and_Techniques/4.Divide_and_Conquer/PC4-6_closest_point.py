import sys
from math import sqrt

def euclidean(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def closest_pair(points):

    n = len(points)//2
    A = [(points[2*i], points[2*i + 1]) for i in range(n)]

    Ax = sorted(A, key = lambda x: x[0])
    Ay = sorted(A, key = lambda x: x[1])

    return 



if __name__ == "__main__":

    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    points = data[1:]

    print(closest_pair(points))
