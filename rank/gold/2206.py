d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def func():
    ans = 10000000
    st = [(0, 0, 0)]
    # 벽을 부셨는지 아닌지에 따라 사용할 3차배열을 생성
    visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    # 시작 위치에 1을 저장
    visited[0][0][0] = 1
    i = 0
    # pop은 시간이 오래걸리기 때문에 인덱스를 1씩 증가시키며 해결
    while i < len(st):
        y, x, u = st[i]
        # y, x가 결과에 도달했으면 return
        if y == N - 1 and x == M - 1:
           return visited[u][y][x]
        # 벽을 뚫는 경우와 뚫지 않는 경우로 경우를 나눠서 계속 반복
        # 지나갈 때마다 +1의 값을 저장하여 도착지점까지 걸린 경로를 계산
        for dy, dx in d:
            if 0 <= y + dy < N and 0 <= x + dx < M:
                if not visited[u][y + dy][x + dx]:
                    if maze[y+dy][x+dx] == '0':
                        visited[u][y+dy][x+dx] = visited[u][y][x] + 1
                        st.append((y+dy, x+dx, u))
                    elif maze[y+dy][x+dx] == '1' and u == 0:
                        visited[1][y+dy][x+dx] = visited[0][y][x] + 1
                        st.append((y+dy, x+dx, u+1))
        # 인덱스 증가
        i += 1
    return -1

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(input()))
result = func()
print(result)
