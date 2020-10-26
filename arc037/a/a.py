n = int(input())
l = list(map(int, input().split()))
ans = 0
for i in range(n):
    ans += max(0, (80 - l[i]))
print(ans)