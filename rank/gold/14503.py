# 로봇청소기의 이동 알고리즘을 구하는 문제
# 조건을 잘 이해하고 구현해보자

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def func(y, x, d):
    val = 1
    while True:
        if not arr[y][x]:
            val += 1
            arr[y][x] = val
        flag = 0
        for i in range(4):
            d -= 1
            if d < 0:
                d += 4
            if 0 <= y+dy[d] < N and 0 <= x+dx[d] < M and arr[y+dy[d]][x+dx[d]] == 0:
                y = y+dy[d]
                x = x+dx[d]
                flag = 1
                break
        if not flag:
            y = y - dy[d]
            x = x - dx[d]
            if 0 <= y < N and 0 <= x < M and arr[y][x] == 1:
                    return val-1

N, M = map(int, input().split())
c, r, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(func(c, r, d))