from sys import stdin

n = int(stdin.readline())
k = int(stdin.readline())

print("YES" if n >= k * 2 else "NO")