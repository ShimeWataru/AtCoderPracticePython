l = list(input().split())
ans = []
for i in range(len(l)):
    tmp = ''
    if l[i] == 'Right':
        tmp = '>'
    elif l[i] == 'Left':
        tmp = '<'
    else:
        tmp = 'A'
    ans.append(tmp)
print(' '.join(ans))
