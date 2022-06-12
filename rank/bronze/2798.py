# 코딩을 시작한지 얼마 안된 나는 왜 이 문제를 어려워했을까 ㅎㅎ
N, M = map(int, input().split())
arr = list(map(int, input().split()))
minV = 300000
ans = 0
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] <= M and M-(arr[i] + arr[j] + arr[k]) < minV:
                ans = arr[i] + arr[j] + arr[k]
                minV = M-(arr[i] + arr[j] + arr[k])
print(ans)