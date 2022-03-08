T = int(input())

for tc in range(T):
    k = int(input())
    n = int(input())
    ARR = [[0]*(n+1) for _ in range(k+1)]
    for i in range(1, n+1):
        ARR[0][i] = i
    if k == 1:
        ARR[1][0] = 0
        for i in range(1, n+1):
            ARR[1][i] = ARR[1][i-1] + ARR[0][i]
    else:
        for i in range(1, k+1):
            ARR[i][0] = 0
            for j in range(1, n+1):
                ARR[i][j] = ARR[i][j-1] + ARR[i-1][j]
    print(ARR[k][n])
