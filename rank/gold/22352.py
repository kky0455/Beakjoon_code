from collections import deque
import sys
input = sys.stdin.readline
# 1차시도 먼저 실험대상과 결과물을 비교하여 불일치 체크, 처음 불일치하는 지점은 저장해두기
# bfs중 백신이 퍼저나가는 지점이지만 이미 실험군과 일치한다 => 바로 실패 리턴
# bfs를 다 돌았다 => 비교용 check리스트를 통해 0의 유무 확인으로 가능성 여부 판단
# --------------------------------------------------------------
# 2차시도 백신을 맞은 부분은 임의의값으로 변한다...?
# -----------------------------------------------------------------
# 3차시도 변환해도 값이 동일할 수 있으니 bfs진행 중 리턴구조 변경
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def zero_check():
    for i in range(N):
        if 0 in check[i]:
            return False
    return True

def bfs():
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and test[ny][nx] == val:
                test[ny][nx] = change_v
                if test[ny][nx] != V[ny][nx]:
                    return print('NO')
                check[ny][nx] = 1
                q.append((ny, nx))
    if zero_check():
        return print('YES')
    else:
        return print('NO')

N, M = map(int, input().split())
test = [list(map(int, input().split())) for _ in range(N)]
V = [list(map(int, input().split())) for _ in range(N)]
check = [[0] * M for _ in range(N)]
q = deque()
val = 0
for i in range(N):
    for j in range(M):
        if test[i][j] == V[i][j]:
            check[i][j] = 1
        else:
            if not q:
                q.append((i, j))
                check[i][j] = 1
                val = test[i][j]
                change_v = V[i][j]
                test[i][j] = change_v

bfs()