N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
# 아래로 쭉 탐사해서 채취하는 자원 누적합
for _ in range(1, N):
    arr[_][0] += arr[_-1][0]
# 우측으로 쭉 탐사해서 채취하는 자원 누적합
for _ in range(1, M):
    arr[0][_] += arr[0][_-1]
# (1, 1)에서 (N-1, M-1)까지 가며 위, 왼쪽을 봐서 더 많은 자원 수를 현재 위치에 더한다
for i in range(1, N):
    for j in range(1, M):
        if arr[i-1][j] >= arr[i][j-1]:
            arr[i][j] += arr[i-1][j]
        else:
            arr[i][j] += arr[i][j-1]
print(arr[N-1][M-1])