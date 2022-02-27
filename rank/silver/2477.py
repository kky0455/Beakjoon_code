N = int(input())

L = []
EW = 0
NS = 0
for i in range(6):
    a, b = map(int, input().split())
    L.append(b)
    if a == 1 or a == 2:
        if b > EW:
            EW = b
    else:
        if b > NS:
            NS = b
A = EW * NS
B = L[L.index(EW)-3] * L[L.index(NS)-3]
print((A - B)*N)