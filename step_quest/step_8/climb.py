a, b, c = map(int, input().split())

e = c - a
f = a - b
g = e//f
if e >= 0:
    print(1)
elif g == 0:
    print(2)
elif e/f == g:
    print(g+1)
elif e/f > g:
    print(g+2)
