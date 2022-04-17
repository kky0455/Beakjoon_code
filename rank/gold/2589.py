dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# dx, dy를 미리 선언하고 문제를 풀어야 시간이 적게 소요됩니다
# L인 위치마다 visited를 생성하고 bfs를 진행해 답을 찾는 방식
def bfs(c_y, c_x):
    global result
    visited = [[0] * M for _ in range(N)]
    Q = [(c_y, c_x)]
    visited[c_y][c_x] = 1
    while Q:
        y, x = Q.pop(0)
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and arr[ny][nx] == 'L':
                Q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1

    if result < visited[y][x]:
        result = visited[y][x]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            bfs(i, j)
print(result-1)