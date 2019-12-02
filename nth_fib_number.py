n = int(input())
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return (n-1)+(n-2)
print(fib(n))
