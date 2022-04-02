def find(y, x):
    global result
    cnt = 0
    block = arr[y][x] #기준점 B, W를 판단하려고
    for i in range(8):
        if i % 2: # i 홀수
            for j in range(8):
                if j % 2:
                    if arr[y+i][x+j] != block:
                        cnt += 1
                else:
                    if arr[y+i][x+j] == block:
                        cnt += 1
        else: # i 짝수
            for j in range(8):
                if j % 2:
                    if arr[y+i][x+j] == block:
                        cnt += 1
                else:
                    if arr[y+i][x+j] != block:
                        cnt += 1
    if cnt < result:
        result = cnt
    if 64 - cnt < result:
        result = 64 - cnt

N, M = map(int, input().split())
result = 1000000000
arr = []
for i in range(N):
    arr.append(list(input()))
for i in range(0, N-7):
    for j in range(0, M-7):
        find(i, j)
print(result)