A = []
for i in range(9):
    A.append(int(input()))
A.sort()
a = sum(A)
for i in A:
    s = a - i - 100
    if s in A:
        a = i
        break
for i in A:
    if i != a and i != s:
        print(i)