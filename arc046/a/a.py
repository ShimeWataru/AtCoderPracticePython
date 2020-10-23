n = int(input())
tmp = 0
cnt = 0
while (True):
  tmp += 1
  if len(set(str(tmp))) == 1:
    cnt += 1
    if cnt == n:
      break
print(tmp)
