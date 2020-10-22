n = int(input())
r = 0
b = 0
for i in range(n):
    s = input()
    r += s.count('R')
    b += s.count('B')
if r > b:
    print('TAKAHASHI')
elif b > r:
    print('AOKI')
else:
    print('DRAW')
