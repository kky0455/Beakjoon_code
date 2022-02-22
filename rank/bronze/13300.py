N, K = map(int, input().split())

lst = [[0]*7 for _ in range(2)]
total = 0
for i in range(N):
    S , Y = map(int, input().split())
    lst[S][Y] += 1

for i in lst:
    for j in range(1, len(i)):
        if i[j] % K == 0:
            total += i[j]//K
        else:
            total += i[j]//K + 1
print(total)