N = int(input())
lst = []
for i in range(N):
    lst.append(input())
a = len(lst[0])
b = set()
for i in range(a):
    c = lst[0]
    for j in range(0, N):
        if c[i] != lst[j][i]:
            b.add(i)
for i in range(a):
    if i in b:
        print('?', end='')
    else:
        print(lst[0][i], end='')