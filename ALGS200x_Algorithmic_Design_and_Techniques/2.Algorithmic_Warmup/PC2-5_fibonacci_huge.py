# Uses python3
import sys

# Solution provided:
'''
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
'''

def get_fibonacci_huge(n, m):
    """
    d = {0:0, 1:1}
    def fib(n):
        if n in d: return d[n]
        else:
            d[n] = fib(n-1) + fib(n-2)
            return d[n]
    """

    def fib(n, m):
        if n < 2: return n

        results = [1, 1]
        for _ in range(n - 2):
            results.append((results[-1] + results[-2]) % m)

        return results[-1]


    def pisano_period(m):
        """
        This returns the Pisano period
        relative to the divisor 'm'.
        """
        previous = 1
        current = 1

        result = 1
        while not (previous == 0 and current == 1):
            previous, current = current, (previous + current) % m
            result += 1

        return result

    return fib(n%pisano_period(m), m)

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
