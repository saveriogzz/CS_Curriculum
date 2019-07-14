# Uses python3
# Solution provided:

"""
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

n = int(input())
print(calc_fib(n))
"""

d = {0:0, 1:1}
def fib_recur(n,d):
    if n in d:
        return d[n]
    else:
        d[n] = fib_recur(n-1,d) + fib_recur(n-2,d)
        return d[n]


n = int(input())
print(fib_recur(n,d))
