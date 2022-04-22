ARR = [[0]*1001 for _ in range(1001)]
N = int(input())
val = 1
for i in range(N):
    x, y, W, H = map(int,input().split())
    for j in range(y, y+H):
        ARR[j][x: x+W] = [val] * W
    val += 1

for i in range(N):
    cnt = 0
    for j in range(1001):
        cnt += ARR[j].count(i+1)
    print(cnt)
