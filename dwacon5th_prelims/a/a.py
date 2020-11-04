import statistics
n = int(input())
l = list(map(int, input().split()))
cnt = [0] * n

ave = statistics.mean(l)

for i in range(n):
    cnt[i] = abs(l[i] - ave)

min_cnt = min(cnt)

for i in range(n):
    if cnt[i] == min_cnt:
        print(i)
        break
