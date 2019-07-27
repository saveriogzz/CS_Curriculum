import sys

def merge(B, C):

    D = []
    inversions = 0
    while B[:] and C[:]:
        b, c = B[0], C[0]

        if b <= c:
            D.append(b)
            B.remove(b)

        else:
            D.append(c)
            C.remove(c)
            inversions += 1

    D.extend(B[:])
    D.extend(C[:])

    return D


def merge_sort(A):
    """Returns the numbers of inversions
        to be performed on an unsorted array:
        0 if sorted, n(n-1)/2 if in reverse order."""

    if len(A) == 1: return A

    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])

    merged = merge(left, right)

    return merged


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    array = data[1:]
    print(merge_sort(array))
