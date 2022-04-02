import math
def difference(n,arr):
 
    d1 = 0
    d2 = 0
 
    for i in range(0, n):
     
        for j in range(0, n):
         
            if (i == j):
                d1 += arr[i][j]
 
            if (i == n - j - 1):
                d2 += arr[i][j]
    return abs(d1 - d2);
 
# Driver Code
n = int(input())
 
arr = []
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))
print(difference(n,arr))