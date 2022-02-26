N = int(input())
lst = [N]
result = []
for i in range(1, N+1):
    l = lst[::]
    l.append(i)
    i = 1    
    while True:
        a = l[i-1] - l[i]
        if a < 0:
            break
        else:
            l.append(a)
        i += 1
    if len(l) > len(result):
        result = l
print(len(result))
print(*result)