lst = [[0]* 100 for _ in range(100)]
T = int(input())
cnt = 0
for tc in range(T):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            if lst[i][j] == 0:
                cnt += 1
                lst[i][j] = 1
print(cnt)