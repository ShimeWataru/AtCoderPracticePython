n = int(input())
l = [int(input()) for i in range(n)]
if n <= 2:
    print(max(l))
elif n == 3:
    print(max(max(l), sum(l) - max(l)))
else:
    ans = 99999999
    for i in range(2 ** 4):
        a = []
        b = []
        for j in range(4):
            if ((i >> j) & 1):
                a.append(l[j])
            else:
                b.append(l[j])
        ans = min(ans, max(sum(a), sum(b)))
    print(ans)