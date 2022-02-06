num = int(input())
n = 0
for i in range(1,num+1):
    if i < 100:
        n += 1
    else:
        a = list()
        for j in str(i):
             a.append(j)
        if int(a[0]) - int(a[1]) == int(a[1]) - int(a[2]):
            n += 1
print(n)