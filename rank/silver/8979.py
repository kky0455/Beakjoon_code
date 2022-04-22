# 정직하게 조건문을 구현해도 맞는 문제, 더 간단하게 맞는 방법은 찾아봐야할 듯

N, K = map(int, input().split())
rank = [0] * (N+1)
arr = []
for i in range(N):
    c, g, s, b = map(int, input().split())
    arr.append((c, g, s, b))

for i in range(N):
    cnt = 1
    for j in range(N):
        if arr[i][1] < arr[j][1]:
            cnt += 1
            continue
        elif arr[i][1] > arr[j][1]:
            continue
        else:
            if arr[i][2] < arr[j][2]:
                cnt += 1
                continue
            elif arr[i][2] > arr[j][2]:
                continue
            else:
                if arr[i][3] < arr[j][3]:
                    cnt += 1
                    continue
                elif arr[i][3] > arr[j][3]:
                    continue
    rank[arr[i][0]] = cnt
print(rank[K])
