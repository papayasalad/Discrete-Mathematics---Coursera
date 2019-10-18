
# Concentration for galton board
# Calculate n choose k
def nCk(n, k):
  if k == 0:
    return 1
  else:
    return n / k * nCk(n - 1, k - 1)

# what is the fraction of beans 40 - 60 among 100 layers?
res = 0
for i in range(39, 60):
  res += nCk(99, i)
print(res / (2**99))  
#0.9647997997822952

# what is the fraction of beans 400 - 600 among 1000 layers?
res = 0
for i in range(399, 600):
  res += nCk(999, i)
print(res / (2**999)) 

print(12/14 + 3/16)
print(2/14 + 13/16)