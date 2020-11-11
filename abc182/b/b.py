def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

n = int(input())
l = list(map(int, input().split()))
ans = [0] * 1001
tmp = []
for i in range(n):
    tmp += list(set(prime_factor(l[i])))
for i in range(len(tmp)):
    ans[tmp[i]] += 1
for i in range(len(ans)):
    if ans[i] == max(ans):
        print(i)
        break
