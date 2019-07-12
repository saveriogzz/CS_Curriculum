# Uses python3
import sys

# Solution Provided
'''
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
'''

def gcd(a,b):
    if a % b == 0: return b
    return gcd(b, a % b)

# Using the mathematical relationship that the product of two numbers
# is equal to the product of the Greatest Common Divisor and the Least Common Multiplier
# of those two numbers: A * B = GCD(A,B) * LCM(A,B)


def lcm(a, b):
    return ((a*b) // gcd(a,b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

