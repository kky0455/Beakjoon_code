from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def func():
    q = deque([(0, 0)])
    arr[0][0] = 2
    while q:
        c_y, c_x = q.popleft()
        for i in range(4):
            y = c_y + dy[i]
            x = c_x + dx[i]
            if 0 <= y < N and 0 <= x < M and arr[y][x] == 0:
                    arr[y][x] = 2
                    q.append((y, x))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
func()

