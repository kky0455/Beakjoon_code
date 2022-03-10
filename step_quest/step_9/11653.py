def NUM(ARR, N):
    for i in range(2, N+1):
        if ARR[i] == 1:
            n = i + i
            while n <= N:
                ARR[n] = 0
                n += i


N = int(input())
if N == 1:
    pass
else:
    ARR = [1] * (N+1)
    NUM(ARR, N)
    lst = []
    for i in range(2, N+1):
        if ARR[i] == 1:
            lst.append(i)
    while N not in lst:
        for i in lst:
            if N % i == 0:
                print(i)
                N = N / i
                break

    print(int(N))
