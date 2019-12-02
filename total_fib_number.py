def fib(num):
  if num == 0:
    return 0
  elif num == 1:
    return 1
  else:
    return fib(num-1)+fib(num-2)
#print(fib(29))
total = 0
for num in range(10):
  total+=fib(num)
print(total)
