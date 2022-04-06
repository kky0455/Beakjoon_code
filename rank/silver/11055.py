def func(v, sumV, idx):
    global result
    if idx == A-1:
        return
    for i in range(idx+1, A):
        if arr[i] > v:
            visited[i] = 1
            func(arr[i], sumV + arr[i], i)
    if result < sumV:
        result = sumV
        
A = int(input())
result = 0
arr = list(map(int, input().split()))
visited = [0] * A
for i in range(A):
    if not visited[i]:
        visited[i] = 1
        func(arr[i], arr[i], i)
print(result)