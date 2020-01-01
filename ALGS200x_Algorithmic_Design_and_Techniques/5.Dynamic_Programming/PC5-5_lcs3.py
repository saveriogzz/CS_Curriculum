


def lcs3(A,B,C):
    """Function too find longest common subsequence
    in three sequences using dynamic programming."""
    m, n, l = len(A), len(B), len(C)
    L = [[[0 for _ in range(m+1)] for _ in range(n+1)] for _ in range(l+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            for k in range(1, l+1):
                if A[i-1] == B[j-1] == C[k-1]:
                    L[i][j][k] = L[i-1][j-1][k-1] + 1
                else:
                    L[i][j][k] = max(L[i-1][j][k], L[i][j-1][k], L[i][j][k-1])

    return L[-1][-1][-1]


if __name__ == '__main__':
    input()
    A = [int(x) for x in input().split()]
    input()
    B = [int(x) for x in input().split()]
    input()
    C = [int(x) for x in input().split()]

    print(lcs3(A,B,C))
