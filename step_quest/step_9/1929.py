def num(ARR, N):
    for i in range(2, N+1):
        if ARR[i] == 1:
            n = 2*i
            while n <= N:
                ARR[n] = 0
                n += i

M, N = map(int, input().split())
ARR = [1] * (N+1)
num(ARR, N)
ARR[1] = 0
for i in range(M, N+1):
    if ARR[i] == 1:
        print(i)
