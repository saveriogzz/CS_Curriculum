import sys


def editing_distance(A, B):
    matrix = [[x for x in range(len(B)+1)]]
    for k in range(1, len(A)+1):
        matrix.append([k] + [0]*len(B))

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            if A[i-1] == B[j-1]:
                matrix[i][j] = min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1])
            else:
                matrix[i][j] = min(matrix[i][j-1]+1, matrix[i-1][j]+1, matrix[i-1][j-1]+1)

    return matrix[-1][-1]




if __name__ == '__main__':
    data = list(map(str, sys.stdin.read().split()))
    A, B = data[0], data[1]
    print(editing_distance(A,B))
