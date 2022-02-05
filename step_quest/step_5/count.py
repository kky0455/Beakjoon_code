num = list()
for i in range(3):
    a = int(input())
    num.append(a)
a = 1
for i in num:
    a *= i
b = str(a)
for i in range(10):
    print(b.count(str(i)))