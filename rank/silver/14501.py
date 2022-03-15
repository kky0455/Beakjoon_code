def fibo(n, max_V):
    global lst
    global val
    if n == N-1:
        if lst[n][0] != 1:
            return 0
        else:
            return max_V + lst[n][1]
    elif n + lst[n][0] >= N:
        return max_V + fibo(n+1, max_V)
    else:
        if lst[n][1] + fibo(n + lst[n][0]-1, max_V) > fibo(n+1, max_V):
            return max_V + lst[n][1] + fibo(n + lst[n][0]-1, max_V)
        else:
            return max_V + fibo(n+1, max_V)

    
    

N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
val = [0] * N
fibo(1, 0)