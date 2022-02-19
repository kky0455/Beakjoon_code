N = int(input())
F = int(input())
lst = [[0]*N for _ in range(N)]
x = y = N//2
lst[N//2][N//2] = 1
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
cnt = 0
n = 1
num = 2
end = N**2+1
while num < end:
    d = cnt % 4
    if num < end:
        for i in range(n):
            x += dx[d]
            y += dy[d]
            lst[y][x] = num
            num += 1
            if num == end:
                break
        cnt += 1
        d = cnt % 4
    if num < end:
        for i in range(n):
            x += dx[d]
            y += dy[d]
            lst[y][x] = num
            num += 1
            if num == end:
                break

    n += 1
    cnt += 1
for i in lst:
    print(*i)
for i in range(N):
    for j in range(N):
        if lst[i][j] == F:
            print(i+1, j+1)