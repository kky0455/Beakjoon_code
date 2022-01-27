num = int(input())
a = ' '
b = '*'
n = 1
for i in range(1, num+1):
    print(a*(num-n)+b*n)
    n += 1