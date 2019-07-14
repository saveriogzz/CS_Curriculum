# Uses python3
import sys

# Solution provided:
"""
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
"""

# Using the fact that the last digits of Fibonacci numbers follow a series,
# which repeats itself every 60 occurrences:

first_60_last = {0:0, 1:1}

def first_60_fib(n, d):
    if n in d: return d[n]
    else:
        d[n] = (first_60_fib(n-1, d) + first_60_fib(n-2, d)) % 10
        return d[n]

first_60_fib(60, first_60_last)

def get_fibonacci_last_digit(n, d):
    if n in range(61):
        return d[n]
    if n > 60:
        return d[n % 60]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n, first_60_last))