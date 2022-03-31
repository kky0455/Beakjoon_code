def mun(idx, r, g, b, cnt):
    global result
    if cnt > 1:
        re = abs(r//cnt - gom[0]) + abs(g//cnt - gom[1]) + abs(b//cnt - gom[2])
        if re < result:
            result = re
    for i in range(idx, N):
        if cnt < 7:
            mun(i + 1, r + lst[i][0], g + lst[i][1], b + lst[i][2], cnt + 1)

N = int(input())
result = 1000
lst = [255, 255, 255]
lst = [list(map(int, input().split())) for _ in range(N)]
gom = list(map(int, input().split()))
mun(0, 0, 0, 0, 0)
print(result)