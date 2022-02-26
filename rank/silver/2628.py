row = [0]
col = [0]

a, b = map(int, input().split())
col.append(a)
row.append(b)

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    if a == 0:
        row.append(b)
    else:
        col.append(b)
row.sort()
col.sort()
maxV = 0
for i in range(len(col)-1):
    a = col[i+1] - col[i]
    for j in range(len(row)-1):
        b = row[j+1] - row[j]
        if a*b > maxV:
            maxV = a*b
print(maxV)