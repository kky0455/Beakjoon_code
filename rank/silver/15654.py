def func(cnt):
    global N, M
    if cnt == M:
        print(*result)
        return
    for i in lst:
        if c[i] == 0:
            c[i] = 1
            result.append(i)
            func(cnt+1)
            result.pop()
            c[i] = 0



N, M = map(int, input().split())
result = []
lst = list(map(int, input().split()))
lst.sort()
c = [0 for _ in range(max(lst)+1)]
func(0)