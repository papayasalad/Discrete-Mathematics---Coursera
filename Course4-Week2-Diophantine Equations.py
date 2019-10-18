# Given three integers a>0, b>0 and c, return some integer x and y 
# such that ax + by = c.  Use Euclid's algorithm to solve it efficiently.
def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)

# return (x, y) such that a * x + b * y = c
def diophantine(a, b, c):
  d = gcd(a, b)
  assert c % d == 0

  x, y = 0, 0
  flag = False
  while not flag:
    if a * x + b * y == d:
      flag = True
    else:
      if x > 0:
        x = -1 * x
      else:
        x = -1 * x + 1
        
    if ((d - a * x) / b).is_integer():
      y = (d - a * x) // b
  
  return (c//d*x, c//d*y)

# test
# 1) 10x + 6y = 14, x = -7, y = 14
# 2) 391x + 299y = -69, x = 9, y = -12
print(diophantine(10, 6, 14) == (-7, 14))
print(diophantine(391, 299, -69) == (9, -12))