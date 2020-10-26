from sys import stdin

n = int(stdin.readline())
a = -1
b = -1

for i in range(1, 38):
    for j in range(1, 26):
        if 3 ** i + 5 ** j == n:
            print(i, j)
            exit()
print(-1)