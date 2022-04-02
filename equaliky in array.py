import math
def array(n,arr):
    max=0
    for i in range(n):
        if (max<arr[i]):
            max=arr[i]
    return n-max
n = int(input())
arr = list(map(int, input().rstrip().split()))
print(array(n,arr))