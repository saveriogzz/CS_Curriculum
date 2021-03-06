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

# Knowing that Pisano Period
# of modulo 10 is 60:

def fibonacci_sum(n):

    def pisano_period(m):
        previous = 1
        current = 1
        result = 1
        while not (previous == 0 and current == 1):
            previous, current = current, (previous + current) % m
            result += 1
        return result

    pisano = pisano_period(10)

    if n < 2: return n

    n %= pisano
    fib_arr = [1,1]
    for _ in range(n):
        fib_arr.append((fib_arr[-1] + fib_arr[-2]) % 10)
    return (fib_arr[-1] - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
