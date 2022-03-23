def func(cnt):
    if cnt == M:
        print(*lst)
        return
    for i in range(N):
        if not lst:
            lst.append(i+1)
            che[i] = 1
            func(cnt+1)
            lst.pop()
            che[i] = 0
        else:
            if i+1 > max(lst):
                lst.append(i+1)
                che[i] = 1
                func(cnt+1)
                lst.pop()
                che[i] = 0


N, M = map(int, input().split())
lst = []
che = [0] * N
func(0)