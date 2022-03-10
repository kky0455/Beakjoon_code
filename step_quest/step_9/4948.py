def num(ARR, N):
    for i in range(2, 2*N+1):
        if ARR[i] == 1:
            n = 2*i
            while n <= 2*N:
                ARR[n] = 0
                n += i

while True:
    N = int(input())
    if N == 1:
        print(1)
    elif N == 0:
        break
    else:
        ARR = [1] * (2*N+1)
        num(ARR, N)
        cnt = 0
        for i in range(N+1, 2*N+1):
            if ARR[i] == 1:
                cnt += 1
        print(cnt)