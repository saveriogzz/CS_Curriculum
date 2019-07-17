# Uses python3
import sys

def get_change(m):
    denominations = [10, 5, 1]

    money_count = 0
    for value in denominations:
        r = m//value
        money_count += r
        m -= r*value

    return money_count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
