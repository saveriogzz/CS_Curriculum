# Uses python3
import sys

# Solution provided:
"""
def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10
"""

def fibonacci_sum(n):
    if n < 2: return n

    fib_arr = [1,1]
    for _ in range(n-2):
        fib_arr.append(fib_arr[-1] + fib_arr[-2])
    return fib_arr[-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
