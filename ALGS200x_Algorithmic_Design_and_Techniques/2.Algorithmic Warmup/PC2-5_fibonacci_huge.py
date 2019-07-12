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
    d = {0:0, 1:1}
    def fib(n):
        if n in d: return d[n]
        else:
            d[n] = fib(n-1) + fib(n-2)
            return d[n]

    if m % 2 == 0:
        r = fib(n%(4*m)) % m
        return r
    else:
        r = fib(n%(2*(m+1))) % m
        return r

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
