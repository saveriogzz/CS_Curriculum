import sys

def maxSalary(numbers):

    def greatOrEqual(number, max_number):
        pass

    result = []

    while numbers:
        max_number = -float('Inf')

        for number in numbers[:]:
            if greatOrEqual(number, max_number):
                max_number = number
        result.append(max_number)
        numbers.remove(max_number)

    return (''.join(str(e) for e in result))


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    numbers = data[1:]
    print(maxSalary(numbers))
