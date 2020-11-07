n, m = map(int, input().split())
s = input()
tab = 1
ans = 0
for i in range(n):
    tab += 1 if s[i] == '+' else -1
    if tab > m:
        tab = 1
        ans += 1
print(ans)