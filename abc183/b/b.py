a, b, c, d = map(int, input().split())
yy = (b / d)
xx = c - a
x = a + xx / (yy + 1) * yy
print(x)

