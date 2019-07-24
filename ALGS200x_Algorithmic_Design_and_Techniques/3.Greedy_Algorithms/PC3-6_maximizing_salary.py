import sys

def maxSalary(numbers):

    def greatOrEqual(number, max_number):
        combination1 = int(str(number) + str(max_number))
        combination2 = int(str(max_number) + str(number))

        if combination1 >= combination2: return True
        else: return False

    result = []

    while numbers:
        max_number = min(numbers)

        for number in numbers[:]:
            if greatOrEqual(number, max_number):
                max_number = number
        result.append(max_number)
        numbers.remove(max_number)

    return (''.join(str(e) for e in result))


if __name__ == "__main__":
    numbers = list(map(int, sys.stdin.read().split()))
    print(maxSalary(numbers))
