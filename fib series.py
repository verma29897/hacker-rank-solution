def fib(n):
    n1=0
    n2=1
    if(n<1):
      return
    print(n1,end=" ")
    for i in range(1,n):
        print(n2,end=" ")
        next=n1+n2
        n1=n2
        n2=next
      
n=int(input())
fib(n)