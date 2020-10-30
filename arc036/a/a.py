from sys import stdin

n, k  = map(int, stdin.readline().split())
l = [int(input()) for i in range(n)]

ans = -1
for i in range(2, n):
    if k > sum([l[i - 2], l[i - 1], l[i]]):
        ans = i + 1
        break
print(ans)