# 아마 1인 좌표를 한번에 담고 not visited만 조사한다면 더 빠른 결과가 나올 것 같다.

def func(c_y, c_x):
    global result
    # 1인 좌표를 Q에 넣고 bfs진행
    Q = [(c_y, c_x)]
    visited[c_y][c_x] = 1
    while Q:
        y, x = Q.pop(0)
        # 8방향으로 탐색
        for dy, dx in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
            n_y = y + dy
            n_x = x + dx
            if 0 <= n_y < N and 0 <= n_x < M:
                # 만약 처음 방문했다면 pop한 좌표의 값에 +1
                if not visited[n_y][n_x]:
                    visited[n_y][n_x] = visited[y][x] + 1
                    Q.append((n_y, n_x))
                # 1인 지점에 따라 여러번 진행하므로 만약 안전거리가 기존 visited에 저장된 값보다 작다면 값 교체
                if visited[n_y][n_x] > visited[y][x] + 1:
                    visited[n_y][n_x] = visited[y][x] + 1
                    Q.append((n_y, n_x))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
# 1인 지점을 찾아서 bfs 진행
for i in range(N):
    if 1 in arr[i]:
        for j in range(M):
            if arr[i][j] == 1:
                func(i, j)
maxV = 0
# visited를 조사해서 가장 큰 값을 탐색해 결과 출력
for i in range(N):
    for j in range(M):
        if visited[i][j] > maxV:
            maxV = visited[i][j]
print(maxV-1)