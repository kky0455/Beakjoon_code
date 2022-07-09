N = int(input())
arr = []
cnt = 1

for _ in range(N):
    arr.append(int(input()))
val = arr[-1]

for i in range(N-2, -1, -1):
    if arr[i] > val:
        val = arr[i]
        cnt += 1

print(cnt)