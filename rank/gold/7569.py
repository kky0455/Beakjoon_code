from collections import deque
import sys
input = sys.stdin.readline
d = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
# bfs문제, 각 시작을 모두 q에 담아 bfs를 진행합니다.
# 익은 토마토는 n_q에 저장했다가 다음에 다시 구합니다.
def check():
    for i in range(H):
        for j in range(N):
            if 0 in Tomato[i][j]:
                return False
    return True


def bfs():
    q = deque([])
    maxV = 1
    for i in range(H):
            for j in range(N):
                for k in range(M):
                    if Tomato[i][j][k] == 1:
                        q.append((i, j, k))
    while True:
        n_q = deque([])
        while q:
            z, y, x = q.popleft()
            for dz, dy, dx in d:
                if 0 <= z+dz < H and 0 <= y+dy < N and 0 <= x+dx < M and not Tomato[z+dz][y+dy][x+dx]:
                    Tomato[z+dz][y+dy][x+dx] += Tomato[z][y][x] + 1
                    n_q.append((z+dz, y+dy, x+dx))
        if n_q:
            q = n_q
            maxV += 1
        else:
            if check():
                return maxV-1
            else:
                return -1


M, N, H = map(int, input().split())
Tomato = [[] for _ in range(H)]
for i in range(H):
    for j in range(N):
        Tomato[i].append(list(map(int, input().split())))
print(bfs())