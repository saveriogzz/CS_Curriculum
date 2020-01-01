import sys

def lcs(A, B):
    """Function to find longest common subsequences
    in two words, using dynamic programming."""

    m, n = len(A), len(B)
    L = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if A[i-1] != B[j-1]:
                L[i][j] = max(L[i-1][j], L[i][j-1])
            else:
                L[i][j] = L[i-1][j-1] + 1
                
    return L[-1][-1]



if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    A, B = data[1:data[0]+1], data[data[0]+2:]
    print(lcs(A,B))
