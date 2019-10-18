# dice = [1, 1, 4, 4, 6, 6]
# res = [0 for x in range(len(dice))]
# print(res)
# for i in range(len(dice)):
#   for j in range(i + 1, len(dice)):
#     print(dice[i] + dice[j])

dice = [1, 1, 4, 4, 6, 6]
res = [{0:0} for x in range(len(dice))]
print(res)

a = 3
t = 4

for x, y in res[0].items():
  if y < t:
    res[0].clear()
    res[0][3] = 4
print(res)

strategy = dict()
for i in range(4):
  strategy[i] = (i + 1) % 4

strategy.pop(0)
print(strategy)