# Uses python3
import sys
# Solution Provided:
'''
def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10
'''

def fibonacci_partial_sum(from_, to):
    assert from_ <= to

    def pisano_period(m):
        previous = 1
        current = 1

        result = 1
        while not (previous == 0 and current == 1):
            previous, current = current, (previous + current) % m
            result += 1

        return result

    pisano = pisano_period(10)

    from_, to = map(lambda x: (x % pisano), [from_, to])

    fib_arr_start = [1,1]
    for _ in range(from_):
        fib_arr_start.append((fib_arr_start[-1] + fib_arr_start[-2]) % 10)

    fib_arr_stop = [1,1]
    for _ in range(to):
        fib_arr_stop.append((fib_arr_stop[-1] + fib_arr_stop[-2]) % 10)

    # Array of last digits of cumulative fibonacci
    # must not subtract the very last term, therefore index is "-2"
    return (fib_arr_stop[-1] - fib_arr_start[-2]) % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
