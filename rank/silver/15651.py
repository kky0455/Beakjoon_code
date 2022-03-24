def func(num, cnt):
    if cnt == M:
        print(*lst)
        return
    else:
        for i in range(N):
            lst.append(i+1)
            func(i, cnt+1)
            lst.pop()

N, M = map(int, input().split())
lst = []
func(0, 0)