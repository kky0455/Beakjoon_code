a = input()
b = a.split()

A = int(b[0])
B = int(b[1])
C = int(b[2])

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)
