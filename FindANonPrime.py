# if x is constructed by x = n^2 + n + 41, find x that is not a prime.
import math

flag = False
n = 1
while not flag:
  x = n ** 2 + n + 41
  n += 1
  j = 2
  while j < math.sqrt(x) and not flag:
    if x % j == 0:
      flag = True
      print("Counter example is %d, it can be divided by %d"%(x, j))
    j += 1 