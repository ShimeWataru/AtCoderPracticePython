h, w = map(int, input().split())
l = [input() for i in range(h)]

ans = 0

for i in range(h):
    for j in range(w - 1):
        if l[i][j] == '.' and l[i][j + 1] == '.':
            ans += 1


for i in range(h - 1):
    for j in range(w):
        if l[i][j] == '.' and l[i + 1][j] == '.':
            ans += 1

print(ans)
