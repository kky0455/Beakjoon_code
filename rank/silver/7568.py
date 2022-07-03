N = int(input())
data = []
rank = []
for i in range(N):
    data.append(tuple(map(int, input().split())))
for i in data:
    cnt = 0
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt+1, end=' ')
print()       