def find(num, cnt):
    global N
    global M
    c[num] = True
    cnt += 1
    ans.append(num)
    if cnt == M:
        print(*ans)
        return
    else:
        for i in range(1, N+1):
            if c[i] != True:
                find(i, cnt)
                c[i] = False
                ans.pop()


N, M = map(int, input().split())
c = [False] * (N+1)
ans = []
for i in range(1, N+1):
    find(i,0)
    c[i] = False
    ans.pop()
