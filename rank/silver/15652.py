def func(num, cnt):
    if cnt == M:
        print(*lst)
        return
    else:
        for i in range(N):
            if not lst:
                lst.append(i+1)
                func(i+1, cnt+1)
                lst.pop()
            elif i+1 >= lst[-1]:
                lst.append(i+1)
                func(i+1, cnt+1)
                lst.pop()
    

N, M = map(int, input().split())
lst = []
func(0, 0)