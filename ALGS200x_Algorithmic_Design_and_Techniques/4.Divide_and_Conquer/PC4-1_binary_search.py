import sys

def binary_search(data, targets):
    '''
    Returns the number of queries
    that are present in the array
    in which we search
    '''

    results = []

    for target in targets:
        left, right = 0, len(data) - 1

        while left <= right:
            middle = (left + right) // 2

            if data[middle] == target:
                results.append(middle)
                break

            elif data[middle] < target: left = middle + 1
            else: right = middle - 1

        else: results.append(-1)


    return sum(e >= 0 for e in results)





if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    A = data[1:(n + 1)]
    k = data[(n + 1)]
    B = data[(n + 2):]

    print(binary_search(A, B))
