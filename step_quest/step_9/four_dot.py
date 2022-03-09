lst_x = []
lst_y = []
for i in range(3):
    a, b = map(int, input().split())
    lst_x.append(a)
    lst_y.append(b)
set_x = set(lst_x)
set_y = set(lst_y)
for i in set_x:
    if lst_x.count(i) == 1:
        print(i, end=' ')
for i in set_y:
    if lst_y.count(i) == 1:
        print(i)