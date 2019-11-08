'''
Write a python program with appropriate comments that creates a menu-driven program that allows a user to enter five numbers (integers) and then choose an operation from one of the operations: finding the smallest, largest, sum, average, or end.
'''
def findsmallest(a):
  return min(a)

def findlargest(a):
  return max(a)

def findsum(a):
  return sum(a)

def findaverage(a):
  return sum(a)/len(a)

def theend(a):
  return print("The End")

def funcs():
  print("Choose a function: \n1.Smallest\n2.Largest\n3.Sum\n4.Average\n5.End")

def inputs():
  c = int(input("Enter a integer (It should be between 25 and 250): "))
  while (not (c>=25 and c<=250)):
    print("Number is not between 25 and 250. Please try again!")
    c = int(input("Enter a integer (It should be between 25 and 250): "))
  return c

def main():
  a1 = inputs()
  a2 = inputs()
  a3 = inputs()
  a4 = inputs()
  a5 = inputs()
  a = [a1,a2,a3,a4,a5]
  funcs()
  while True:
    b = int(input("Write yor function number: "))
    if b==1:
      print(findsmallest(a))
    elif b==2:
      print(findlargest(a))
    elif b==3:
      print(findsum(a))
    elif b==4:
      print(findaverage(a))
    elif b==5:
      print(theend(a))
      break

main()
