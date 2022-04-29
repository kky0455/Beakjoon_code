# 로봇청소기의 이동 알고리즘을 구하는 문제, 푸는중

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def func(y, x, d):
    arr[y][x] = 1
    while True:
        flag = 0
        if 0 <= y+dy[d] < N and 0 <= x+dx[d] < M and arr[y+dy[d]][x+dx[d]] == 0:
            arr[y+dy[d]][x+dx[d]] = arr[y][x] + 1
            y = y+dy[d]
            x = x+dx[d]
        else:
            for i in range(3):
                d -= 1
                if d < 0:
                    d += 4
                if 0 <= y+dy[d] < N and 0 <= x+dx[d] < M and arr[y+dy[d]][x+dx[d]] == 0:
                    arr[y+dy[d]][x+dx[d]] = arr[y][x] + 1
                    y = y+dy[d]
                    x = x+dx[d]
                    flag = 1
                    break
            if not flag:
                return arr[y][x]

N, M = map(int, input().split())
c, r, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(func(c, r, d))