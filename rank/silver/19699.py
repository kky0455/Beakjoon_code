def find(idx, sumV, cnt):
    global ans
    if cnt == M:
        if arr[sumV] and sumV not in ans:
            ans.append(sumV)
        return
    if idx == N-1:
        return
    for i in range(idx+1, N):
        if not visited[i]:
            visited[i] = 1
            find(i, sumV+lst[i], cnt+1)
            visited[i] = 0

def prime():
    num = sum(lst[-M:])
    arr = [1] * (num+1)
    for i in range(2, num+1):
        if arr[i]:
            a = 2 * i
            while a < num+1:
                arr[a] = 0
                a += i
    return arr
    
N, M = map(int, input().split())
lst = list(map(int, input().split()))
visited = [0] * N
ans = []
lst.sort()
arr = prime()
for i in range(N):
    visited[i] = 1
    find(i, lst[i], 1)
ans.sort()
if ans:
    print(*ans)
else:
    print(-1)