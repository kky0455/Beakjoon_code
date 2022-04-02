SumV = [[0, 2, 5, 7], [1, 2, 3, 4], [0, 3, 6, 10], [7, 8, 9, 10], [1, 5, 8, 11], [4, 6, 9, 11]]
def check():
    for i in range(6):
        temp = 0
        for j in range(4):
            temp += ans[SumV[i][j]]
        if temp != 26:
            return False
    return True

def find(cnt):
    global result
    if result:
        return
    if cnt == 12:
        if check():
            result = True
            return
        else:
            return
    if ans[cnt]:
        find(cnt + 1)
    else:
        for v in range(1, 13):
            if not visited[v]:
                visited[v] = 1
                ans[cnt] = v
                find(cnt+1)
                if result:
                    return
                ans[cnt] = 0
                visited[v] = 0

Alpha = ['x', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
arr = []
ans = [0] * 12
result = False
s_lst = [[] for _ in range(6)]
visited = [0] * 13
cnt = 0
for i in range(5):
    arr.append(list(input()))
for i in range(5):
    for j in range(9):
        if arr[i][j] != '.':
            ans[cnt] = Alpha.index(arr[i][j])
            visited[Alpha.index(arr[i][j])] = 1
            cnt += 1
find(0)
idx = 0
for i in range(5):
    for j in range(9):
        if arr[i][j] == '.':
            print(arr[i][j], end='')
        else:
            print(Alpha[ans[idx]], end='')
            idx += 1
    print()