T = int(input())
a = list()

for i in range(T):
    a.append(int(input()))


for i in range(T-1):
    min_val = a[i]
    for j in range(i+1, T):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
    print(a[i])
print(a[-1])