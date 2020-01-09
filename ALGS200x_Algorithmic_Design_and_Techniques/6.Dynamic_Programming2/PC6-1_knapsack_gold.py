import sys


def knapsack(n, W):
    """Recursive solution"""
    arr = [[None for _ in range(W+1)] for _ in range(n+1)]

    if arr[n][W] != None: return arr[n][W]
    if n == 0 or W == 0:
        res = 0
    elif weights[n-1] > W:
        res = knapsack(n-1, W)
    else:
        tmp1 = knapsack(n-1, W)
        tmp2 = weights[n-1] + knapsack(n-1, W-weights[n-1])
        res = max(tmp1, tmp2)
    arr[n][W] = res
    return arr[n][W]




if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    W, n = data[0], data[1]
    weights = data[2:]
    print(knapsack(n, W))
