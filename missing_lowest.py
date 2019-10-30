#a is a list of int, we try to find the missing lowest positive number in the list.
def findlowest(a):
  b=1
  while b in a:
    b+=1
  return b

a= list(map(int,input().split()))
print(findlowest(a))
