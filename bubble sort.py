def bubblesort(n,arr):
  count=0
  for i in range(len(arr)):
    for j in range(len(arr)-1):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
        count+=1
      
  print (f'Array is sorted in {count} swaps.')
  print("First Element:",arr[0])
  print("Last Element:",arr[-1])
n=int(input())
arr=list(map(int,input().rstrip().split()))
bubblesort(n,arr)