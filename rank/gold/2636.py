def func():
    Q = [(0, 0)]
    visited[0][0] = 1
    num = 2
    target = [0]
    while True:
        flag = 0
        i = 0
        n_Q = []
        cnt = 0
        while i < len(Q):
            y, x = Q[i]
            for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if 0 <= y+dy < N and 0 <= x+dx < M and not visited[y+dy][x+dx]:
                    if arr[y+dy][x+dx] == 1:
                        cnt += 1
                        arr[y+dy][x+dx] = num
                        n_Q.append((y+dy, x+dx))
                    elif arr[y+dy][x+dx] in target:
                        visited[y+dy][x+dx] = 1
                        if (y+dy, x+dx) not in Q:
                            Q.append((y+dy, x+dx))
            i += 1
        for j in range(N):
            if 1 in arr[j]:
                flag = 1
                break
        if flag:
            visited[n_Q[0][0]][n_Q[0][1]] = 1
            Q = n_Q[::]
            target.append(num)
            num += 1
        else:
            return num-1, cnt



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
time, cnt = func()
print(time)
print(cnt)