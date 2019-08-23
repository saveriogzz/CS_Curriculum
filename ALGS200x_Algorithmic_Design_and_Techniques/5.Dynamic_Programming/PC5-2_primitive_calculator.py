def greedy_calc(n):

    numOperations = 0
    history = [n]

    while n > 1:
        numOperations += 1
        if n % 3 == 0:
            n /= 3
        elif n % 2 == 0:
            n /= 2
        else:
            n -= 1

        history.append(int(n))

    return numOperations, history[::-1]



def min_ops(n):

    result = [0 for x in range(n + 1)]

    for i in range(2, n+1):
        min1 = result[i-1]
        min2 = float('inf')
        min3 = float('inf')
        if i % 2 == 0:
            min2 = result[i // 2]
        if i % 3 == 0:
            min3 = result[i // 3]
        minOp = min(min1, min2, min3)

        result[i] = minOp + 1

    return result[-1]


if __name__ == '__main__':
    n = int(input())
    print(min_ops(n))
