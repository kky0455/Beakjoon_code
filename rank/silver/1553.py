d1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
d2 = [(1, 0), (0, 1)]
# y, x는 인덱스 / cnt는 도미노가 2개의 숫자로 구성되어서 구분하기 위한 용도 / k는 카운팅한 도미노의 개수
def find(y, x, cnt, k):
    global result
    # 도미노의 개수가 28개가 되면 result를 1올리고 return
    if k == 28:
        result += 1
        return
    # 도미노 블록을 완성시킬 숫자 탐색
    if cnt % 2 == 0:
        # 현 위치의 상하좌우 탐색
        for dy, dx in d2:
            a = ''
            # 범위 안에 들어가고 아직 확인되지 않은 곳인지 판단
            if 0 <= y+dy < 8 and 0 <= x + dx < 7 and c_arr[y+dy][x+dx] == 0:
                # 11 00 22 33 같은 형식이 아닐 때
                if arr[y][x] != arr[y+dy][x+dx]:
                    # a 변수에 숫자 두개를 연결
                    a = str(arr[y][x]) + str(arr[y+dy][x+dx])
                    # 이 a 변수가 도미노 블록 리스트에 있는지 판단하여 있다면 그 숫자쌍을 제거하고 다음 탐색 진행
                    if a in lst:
                        c_arr[y+dy][x+dx] = 1
                        lst.remove(a)
                        find(y+dy, x+dx, cnt+1, k+1)
                        lst.append(a)
                        c_arr[y+dy][x+dx] = 0
                    # 회전이 가능하니 숫자를 바꾼 다음에도 체크
                    a = str(arr[y+dy][x+dx]) + str(arr[y][x])
                    if a in lst:
                        c_arr[y+dy][x+dx] = 1
                        lst.remove(a)
                        find(y+dy, x+dx, cnt+1, k+1)
                        # 함수가 끝나고 돌아오면 다시 그 쌍을 lst에 넣어준다.
                        lst.append(a)
                        c_arr[y+dy][x+dx] = 0
                else:
                    a = str(arr[y][x]) + str(arr[y + dy][x + dx])
                    if a in lst:
                        c_arr[y + dy][x + dx] = 1
                        lst.remove(a)
                        find(y + dy, x + dx, cnt + 1, k + 1)
                        lst.append(a)
                        c_arr[y + dy][x + dx] = 0
    # 다음 도미노 블록이 될 시작점 탐색
    else:
        for dy, dx in d1:
            if 0 <= y+dy < 8 and 0 <= x + dx < 7 and c_arr[y+dy][x+dx] == 0:
                c_arr[y+dy][x+dx] = 1
                find(y+dy, x+dx, cnt+1, k)
                c_arr[y+dy][x+dx] = 0

lst = ['00', '01', '02', '03', '04', '05', '06', '11', '12', '13', '14', '15', '16', '22', '23', '24', '25', '26', '33', '34', '35', '36', '44', '45', '46', '55', '56', '66']
arr = [list(map(int, input())) for _ in range(8)]
c_arr = [[0] * 7 for _ in range(8)]
c_arr[0][0] = 1
result = 0
find(0, 0, 0, 0)
print(result)