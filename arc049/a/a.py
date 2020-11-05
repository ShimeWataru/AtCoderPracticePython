s = input()
l = list(map(int, input().split()))
ans = ''

for i in range(len(l)):
    if i == 0:
        ans += s[0:l[i]]
    else:
        ans += s[l[i - 1]:l[i]]
    ans += '"'
ans += s[l[-1]:]
print(ans)

