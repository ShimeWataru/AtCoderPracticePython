# bit 全探索

```python
if ((i >> j) & 1):
```

i を j 回右シフトした際の下一桁が１のとき True を返す

```python
n, m = map(int, input().split())
l = [list(map(int, input().split())) for i in range(m)]
p = list(map(int, input().split()))
ans = 0
for i in range(2 ** n):
    check = True
    for j in range(m):
        light = 0
        for k in range(1, len(l[j])):
            if ((i >> l[j][k] - 1) & 1):
                light += 1
        if light % 2 != p[j]:
            check = False
    if check:
        ans += 1
print(ans)
```
