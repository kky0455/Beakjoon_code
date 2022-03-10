def num(ARR, N, lst):
    for i in range(2, N):
        if ARR[i] == 1:
            lst.append(i)
            n = 2*i
            while n <= N-1:
                ARR[n] = 0
                n += i
    return lst
T = int(input())
for tc in range(T):
    N = int(input())
    ARR = [1]*N
    lst = []
    num(ARR, N, lst)
    min_num = 10000000000
    for i in lst:
        for j in lst:
            if i + j == N and i <= j and min_num > j - i:
                min_num = j - i
                ans_x = i
                ans_y = j

    print(f'{ans_x} {ans_y}')
