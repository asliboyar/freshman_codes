#the code is checking that input - a member of the list and that remainig is in the list or not?.
k=int(input())
arr1=[10,2,4,7,9]
def w(arr1,k):
  for i in range(0,len(arr1)):
    if k-arr1[i] in arr1:
      return True
    else:
      return False
print(w(arr1,k))
