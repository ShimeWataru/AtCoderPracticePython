n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
max_ = 0
for i in range(n):
  max_ = max(max_, sum(l[i][:-1]) + l[i][-1] * 110 / 900)
print(max_)