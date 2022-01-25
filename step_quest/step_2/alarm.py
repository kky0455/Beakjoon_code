a, b = input().split()
a1 = int(a)
b1 = int(b)
b1 -= 45
if b1 < 0:
    b1 += 60
    a1 -= 1
if a1 < 0 :
    a1 += 24

print(a1, b1)
