a, b = input().split()

ans = []
for i in range(3):
    ans.append(int(a[:2 - i] + '9' + a[3 - i:]) - int(b))

for i in range(3):
    ans.append(int(a) - int(b[:2 - i] + '1' +  b[3 - i:]))

ans.append(int(a) - int(b[0] + '0' +  b[2]))
ans.append(int(a) - int(b[0] + b[1] + '0'))
print(max(ans))
