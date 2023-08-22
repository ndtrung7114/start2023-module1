#1
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#2
x = lambda a: a * 3
print(x(3))

#3
def myfunc(n):
  a = 3 * n
  return a

mytripler = myfunc(11)

print(mytripler)




