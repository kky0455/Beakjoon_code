ARR = [[0]*1001 for _ in range(1001)]
N = int(input())
val = N-1
for i in range(N):
    x, y, W, H = map(int,input().split())
    for j in range(W):
        for k in range(H):
            ARR[x+j][y+k] = val
    val += 1
    
for i in range(N):
    cnt = 0
    for j in range(1001):
        for k in range(1001):
            if ARR[j][k] == i+1:
                cnt += 1
    print(cnt)
            