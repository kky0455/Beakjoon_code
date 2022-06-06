# DP문제, 정렬 후 누적합을 구하여 답을 구한다.

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(1, len(arr)):
    arr[i] = arr[i-1] + arr[i]
print(sum(arr))