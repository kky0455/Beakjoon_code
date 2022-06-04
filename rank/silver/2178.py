# bfs복습문제
# 입력을 문자형으로 받기 때문에 시작위치에 1을 넣고 시작한다.
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def bfs():
    q = [(0, 0)]
    maze[0][0] = 1
    while q:
        y, x = q.pop(0)
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == '1':
                maze[ny][nx] = maze[y][x] + 1
                if ny == N-1 and nx == M-1:
                    return 
                q.append((ny, nx))


N, M = map(int, input().split())

maze = [list(input()) for _ in range(N)]
bfs()
print(maze[N-1][M-1])