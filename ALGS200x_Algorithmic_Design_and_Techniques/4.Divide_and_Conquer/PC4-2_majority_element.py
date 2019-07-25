import sys

def majority_element(A):
    # base case:
    if len(A) == 1: return A[0]

    else:
        mid = len(A) // 2
        majority_left = majority_element( A[:mid] )
        majority_right = majority_element( A[mid:] )

    if (majority_left == majority_right): return majority_right
    elif (A.count(majority_left) > (len(A) // 2)): return majority_left
    elif (A.count(majority_right) > (len(A) // 2)): return majority_right
    else: return 'No majority element.'




if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    array = data[1:]

    print(majority_element(array))
