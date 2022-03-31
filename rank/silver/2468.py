d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(c_y, c_x, c_arr):
    st = [(c_y, c_x)]
    while st:
        y, x = st.pop()
        for dy, dx in d:
            if 0 <= y+dy < N and 0 <= x+dx < N and c_arr[y+dy][x+dx] == 0:
                st.append((y+dy, x+dx))
                c_arr[y+dy][x+dx] = 1

def find(maxV):
    global ans
    result = 0
    c_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N): 
            if arr[i][j] < maxV:
                c_arr[i][j] = 1
    for i in range(N):
        for j in range(N):
            if c_arr[i][j] == 0:
                c_arr[i][j] = 1
                dfs(i, j, c_arr)
                result += 1
    if result > ans:
        ans = result

N = int(input())
ans = 0
arr = [list(map(int, input().split())) for _ in range(N)]
maxV = 0
for i in arr:
    if maxV < max(i):
        maxV = max(i)
for i in range(1, maxV+1):
    find(i)
print(ans)