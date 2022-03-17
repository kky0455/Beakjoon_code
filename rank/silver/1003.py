def fibo(n):
    global cnt0
    global cnt1
    if n < len(memo_0):
        cnt0 += memo_0[n]
        cnt1 += memo_1[n]
    else:
        fibo(n-1)
        fibo(n-2)
        memo_0.append(cnt0)
        memo_1.append(cnt1)
T = int(input())
memo_0 = [1, 0]
memo_1 = [0, 1]
for tc in range(T):
    cnt0 = 0
    cnt1 = 0
    N = int(input())
    fibo(N)
    print(f'{memo_0[N]} {memo_1[N]}')