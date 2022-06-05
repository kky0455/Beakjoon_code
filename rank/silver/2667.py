# dfs 복습문제
# 그룹별로 다른 숫자로 카운트 후 그 숫자를 저장하여 출력하자

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(i, j):
    global val
    stack = [(i, j)]
    arr[i][j] = val
    cnt = 1
    while stack:
        y, x = stack.pop()
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < len(arr[0]) and arr[ny][nx] == '1':
                arr[ny][nx] = val
                cnt += 1
                stack.append((ny, nx))
    ans.append(cnt)
    val += 1

N = int(input())
val = 2
ans = []
arr = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(len(arr[i])):
        if arr[i][j] == '1':
            dfs(i, j)
ans.sort()
print(len(ans))
for _ in ans:
    print(_)