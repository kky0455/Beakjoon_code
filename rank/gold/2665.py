dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

from collections import deque
def bfs():
    q = deque([])
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        c_y, c_x = q.popleft()
        for i in range(4):
            y = c_y + dy[i]
            x = c_x + dx[i]
            if 0 <= y < N and 0 <= x < N:
                if arr[y][x] == 1:
                    if visited[y][x] > visited[c_y][c_x] or visited[y][x] == -1:
                        visited[y][x] = visited[c_y][c_x]
                        q.append((y, x))
                else:
                    if visited[y][x] == -1 or visited[y][x] > visited[c_y][c_x]:
                        visited[y][x] = visited[c_y][c_x] + 1
                        q.append((y, x))

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input())))
visited = [[-1] * N for _ in range(N)]
bfs()
print(visited[-1][-1])
