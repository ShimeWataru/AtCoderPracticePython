from sys import stdin

a, k = map(int, stdin.readline().split())
s = 2 * 10 ** 12
cnt = a
d = 0
if k == 0:
    print(s - a)
else:
    while (True):
        if cnt >= s:
            break
        cnt += (1 + k * cnt)
        d += 1
    print(d)
