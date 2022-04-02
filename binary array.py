def countOnes(arr,low,high):
     
    if high>=low:
         
        # get the middle index
        mid = low + (high-low)//2
         
        # check if the element at middle index is last 1
        if ((mid == high or arr[mid+1]==0) and (arr[mid]==1)):
            return mid+1
             
        # If element is not last 1, recur for right side
        if arr[mid]==1:
            return countOnes(arr, (mid+1), high)
             
        # else recur for left side
        return countOnes(arr, low, mid-1)
     
    return 0
n=int(input())
arr=list(map(int,input().rstrip().split()))
print(countOnes(arr, 0 , len(arr)-1))