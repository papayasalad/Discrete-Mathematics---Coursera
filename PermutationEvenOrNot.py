# Write a function to check whether permutation is even
# def is_permutation(p):
#   return (set(p)==set(range(len(p))))
       
# print (is_permutation([0]))
# print (is_permutation([0,2,1]))
# print (is_permutation([1,2,3]))

# print ([0,2,1])
# print (set([0,2,1]))

def is_even(p):
  step = 0
  pos = 0
  n = len(p)

  while pos < n - 1:
    index = pos
    min_val = p[pos]
    min_pos = index
    while index < n - 1:
      index += 1
      if p[index] < min_val:
        min_pos = index
        min_val = p[index] 
    if pos != min_pos:
      p[min_pos] = p[pos]
      p[pos] = min_val
      step += 1
    pos += 1
  return step % 2 == 0    

print(is_even([0,2,1]))
print(is_even( [0,3,2,4,5,6,7,1,9,8]))