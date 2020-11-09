n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
ans = 0
for i in range(n):
    n = l[i][0] - 1
    m = l[i][1]
    ans -= (n ** 2 + n) / 2
    ans += (m ** 2 + m) / 2
print(int(ans // 1))