l = list(map(int,input().split()))
check = False
for i in range(2 ** 4):
    sum_1 = 0
    sum_2 = 0
    for j in range(4):
        if ((i >> j) & 1):
            sum_1 += l[j]
        else:
            sum_2 += l[j]
    if sum_1 == sum_2:
        check = True
print("Yes" if check else "No")