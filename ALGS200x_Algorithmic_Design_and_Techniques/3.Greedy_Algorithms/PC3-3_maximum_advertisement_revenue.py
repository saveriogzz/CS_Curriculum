import sys

def max_dotproduct(a, b):
    a.sort()
    b.sort()

    return sum([x * y for x,y in zip(a, b)])


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    profits = data[1:(n + 1)]
    clicks = data[(n + 1):]
    print(max_dotproduct(profits, clicks))
