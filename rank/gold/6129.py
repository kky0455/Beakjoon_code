d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

from collections import deque


def bfs():
    visited = [[0] * N for _ in range(N)]
    q = deque([])
    y, x = A
    visited[y][x] = 1
    # A지점에서 갈 수 있는 방향을 모두 q에 저장
    for i in range(4):
        if 0 <= y + d[i][0] < N and 0 <= x + d[i][1] < N:
            if arr[y + d[i][0]][x + d[i][1]] == '.':
                q.append((y + d[i][0], x + d[i][1], i))
                visited[y + d[i][0]][x + d[i][1]] = 1
            if arr[y + d[i][0]][x + d[i][1]] == 'B':
                return 0
    while q:
        y, x, dir = q.popleft()
        for i in range(4):
            ny = y + d[i][0]
            nx = x + d[i][1]
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] != 'x':
                # 방문하지 않은 장소일 때
                if not visited[ny][nx]:
                    # 방향이 다르면 +1한 값을 저장
                    if dir != i:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((ny, nx, i))
                    # 방향이 같다면 같은 값을 저장
                    else:
                        visited[ny][nx] = visited[y][x]
                        q.append((ny, nx, i))
                # 방문한 장소일 때
                else:
                    # 방향이 다르고, 방문할 장소의 값이 +1한 값보다 클 때
                    if dir != i and visited[ny][nx] > visited[y][x] + 1:
                        visited[ny][nx] = visited[y][x] + 1
                        q.append((ny, nx, i))
                    # 방향이 같고, 방문한 장소값이 더 클 때
                    elif dir == i and visited[ny][nx] > visited[y][x]:
                        visited[ny][nx] = visited[y][x]
                        q.append((ny, nx, i))
    # B위치에 저장된 값 리턴
    y, x = B
    return visited[y][x] - 1


N = int(input())
arr = [list(input()) for _ in range(N)]
# A, B지점 좌표 입력
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'A':
            A = [i, j]
        if arr[i][j] == 'B':
            B = [i, j]
print(bfs())
