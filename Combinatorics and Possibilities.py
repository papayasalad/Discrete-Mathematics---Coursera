def sum(n, delta):
  if delta == 1:
    return 1
  return n + sum(n - delta, delta - 1)  

#print(sum(36, 8))
#print(sum(999*499, 998))


# Numbers with fixed sum of digits.
count = 0
for n in range(10000):
  digit_sum = 0
  i = n
  while i >= 10:
    digit_sum += i % 10
    i //= 10
  digit_sum += i
  if digit_sum == 10:
    count += 1

print(count)


cnt = 0
for n in range(100, 10000):
  flag = True
  while flag and n >= 10:
    if n % 10 >= n // 10 % 10:
      n = n // 10
    else: 
      flag = False
  if flag:
    cnt += 1
print(cnt)        




