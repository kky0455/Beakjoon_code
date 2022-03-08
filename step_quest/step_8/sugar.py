N = int(input())
a, b = divmod(N, 5)
ans = 0
if b == 0:
    print(a)
else:
    for i in range(a, -1, -1):
        num = N - 5 * i
        c, d = divmod(num, 3)
        if d == 0:
            print(i + c)
            ans = 1
            break
    if ans == 0:
        print(-1)