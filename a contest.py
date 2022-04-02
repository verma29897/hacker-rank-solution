import math
def diff(n,k,arr):
    sum=0
    for i in range(n):
        if (arr[i]>0 and arr[i]>=arr[k-1]):
            sum+=1
    return sum



n,k=map(int,input().split())
arr=list(map(int,input().rstrip().split()))
print(diff(n,k,arr))