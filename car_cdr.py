#there are 2 functions, car and cdr. car finds the first element of pair, cdr finds the second element in pair.
def cons(a,b):
  def pair(f):
    return f(a,b)
  return pair
  
def car(pair):
  return (pair(lambda a, b: a))

def cdr(pair):
  return (pair(lambda a, b: b))

print(car(cons(5,4)))
print(cdr(cons(5,4)))
