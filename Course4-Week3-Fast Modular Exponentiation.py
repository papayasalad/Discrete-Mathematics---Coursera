# computes b^(2^k) mod m using only around log2(K) modular multiplications.
def FastModularExponentiation(b, k, m):
  # your code here
  i = 1
  
  while i <= k:
    b = b * b % m
    i = i + 1
  
  return b

#Test
#assert(FastModularExponentiation(7, 7, 11) == 9)
print(FastModularExponentiation(7, 7, 11))

# Computes b^e mod m using around 2log_2(e) modular multiplications.
def FastModularExponentiation2(b, e, m):
  # your code here
  bin_e = "{0:b}".format(e) #convert e to binary form
  l = len(bin_e)
  
  r = 1
  for i in range(l):
    if bin_e[l - 1 - i] == "1":
      r = r * b % m
    b = b * b % m
  return r 


# In the code below I compute b^(2^0),b^(2^1)...to b^(2^k) mod m for all 2^k <= e in the first for loop and then multiply all results for 2^k in the binary representation of e in the second for loop.
# In the code above I combine these two steps in one for loop.
"""  
  mod_list = [None for _ in range(l)]
  mod_list[0] = b % m
  for i in range(1, l):
    mod_list[i] = mod_list[i - 1]**2 % m
  
  r = 1  
  for i in range(l):
    if bin_e[l - 1 - i] == "1":
      r = r * mod_list[i] % m
 
  return r
"""
print(FastModularExponentiation2(7, 13, 11))
#Test  
#assert(FastModularExponentiation2(7, 13, 11) == 2) 

# In the code below I call the first method FastModularExponentiation(b, k, m)
def FastModularExponentiation3(b, e, m):
  # your code here
  bin_e = bin(e)
  string_e = str(bin_e)[2:]
  res = 1
  for i in range(len(string_e)):
    if string_e[len(string_e) - 1 - i] == '1':
      res = res * FastModularExponentiation(b, i, m)
    res = res % m
  return res
print(FastModularExponentiation3(3, 8, 1000))  
