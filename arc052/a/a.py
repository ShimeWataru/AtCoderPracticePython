s = input()
ans = ''
for i in range(len(s)):
    if s[i] in '0123456789':
        ans += s[i]
print(int(ans))
