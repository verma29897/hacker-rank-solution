import math
def difference(n,arr):
    even=0
    odd=0
    for i in range(n):
        for j in range(n):
           if arr[i][j]%2==0:
               even+=arr[i][j]
           else:
               odd+=arr[i][j]
    print(odd)
    print(even)
    
# Driver Code
n = int(input())
 
arr = []
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))
difference(n,arr)