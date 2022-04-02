def gcd(a,b):
  if a==0:
    return b
  return gcd(b%a,a)
first=input().strip().split()
x=int(first[0])
y=int(first[1])
print(gcd(x,y))
