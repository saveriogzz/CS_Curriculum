# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

# Solution provided:
'''
result = 0

for i in range(0, n):
    for j in range(i+1, n):
        if a[i]*a[j] > result:
            result = a[i]*a[j]

print(result)
'''

a.sort()
print(a[-1] * a[-2])