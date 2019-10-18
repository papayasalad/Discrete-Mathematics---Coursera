# Use extended Euclid's algorithm for finding modular inverses, implement 
# an efficient algorithm for dividing b by a modulo n.
# Given three integers aa, bb, and nn, such that gcd(a,n)=1 and n > 1, 
# the algorithm should return an integer x such that 0 <= x <= n - 1 and 
# b/a=x(mod n) (that is, b=ax(mod n)).

def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  while a > 0 and b > 0:
    if a >= b:
      a = a % b
    else:
      b = b % a
  return max(a, b)
  
def divide(a, b, n):
  assert n > 1 and a > 0 and gcd(a, n) == 1
  
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  s = 0
  flag = False
  while not flag:
    if s > 0:
      s = -1 * s
    else:
      s = -1 * s + 1
      
    if ((1 - a * s) / n).is_integer():
      flag = True
  
  return b * s % n
  
# test
print(divide(2, 7, 9) == 8)  
