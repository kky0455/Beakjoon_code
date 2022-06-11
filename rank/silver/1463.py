# DP복습 문제
# 1부터 목표 수까지 올라가며 최소도달값이 몇이 되나 확인
N = int(input())
arr = [0] * (N+1)
num = 1
while num != N:
    if 0 <= num * 3 <= N:
        if arr[num*3] == 0 or arr[num*3] >= arr[num] + 1:
            arr[num * 3] = arr[num] + 1
    if 0 <= num * 2 <= N:
        if arr[num*2] == 0 or arr[num*2] >= arr[num] + 1:
            arr[num * 2] = arr[num] + 1
    if 0 <= num + 1 <= N:
        if arr[num+1] == 0 or arr[num+1] >= arr[num] + 1:
            arr[num + 1] = arr[num] + 1
    num += 1
print(arr[N])