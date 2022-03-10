def num(lst, N):
    for i in range(2, N+1):
        if lst[i] == 0:
            pass
        else:
            n = i + i
            while n <= N:
                lst[n] = 0
                n += i

M = int(input())
N = int(input())
lst = [1] * (N+1)
num(lst, N)
min_num = 10001
sum = 0
lst[1] = 0
for i in range(M, N+1):
    if lst[i] == 1:
        sum += i
        if min_num > i:
            min_num = i
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min_num)