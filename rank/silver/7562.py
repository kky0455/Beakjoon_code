m = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
def find(y, x):
    # 목적지와 현재위치의 관계에 따라 조사할 지점 생성
    global e_y, e_x
    if y < e_y and x < e_x:
        return [1, 2, 3, 4]
    elif y > e_y and x < e_x:
        return [7, 0, 1, 2]
    elif y < e_y and x > e_x:
        return [3, 4, 5, 6]
    elif y > e_y and x > e_x:
        return [5, 6, 7, 0]
    elif y == e_y and x < e_x:
        return [0, 1, 2, 3]
    elif y == e_y and x > e_x:
        return [4, 5, 6, 7]
    elif y < e_y and x == e_x:
        return [2, 3, 4, 5]
    elif y > e_y and x == e_x:
        return [6, 7, 0, 1]



def func():
    global result
    # Q에 시작점 넣어두기
    Q = [(s_y, s_x)]
    # pop을 쓰면 시간이 오래걸리므로 idx를 증가시키며 탐색
    idx = 0
    while idx < len(Q):
        # idx가 Q리스트의 길이보다 작은동안 == 참조할 수 있는 동안
        c_y, c_x = Q[idx]
        # 목적지에 도달한 상황에서의 if문
        if c_y == e_y and c_x == e_x:
            result = visited[c_y][c_x] - 1
            idx += 1
            continue
        # 백트래킹 과정
        if result <= visited[c_y][c_x] - 1:
            idx += 1
            continue
        # 8방향은 너무 많으니 4방향으로 단축시키기
        lst = find(c_y, c_x)
        # 구한 4개의 방향에서 탐색 진행
        for i in lst:
            y = c_y + m[i][0]
            x = c_x + m[i][1]
            if 0 <= y < l and 0 <= x < l:
                if not visited[y][x]:
                    # 조건에 만족하는 좌표를 Q에 append
                    visited[y][x] = visited[c_y][c_x]+1
                    Q.append((y, x))
        idx += 1

T = int(input())
for tc in range(1, T+1):
    result = 100000000000
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    s_y, s_x = map(int, input().split())
    e_y, e_x = map(int, input().split())
    visited[s_y][s_x] = 1
    func()
    print(result)