T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    a = str(a)
    a = a[-1]
    a = int(a)
    c = [a]

    for i in range(b):
        a *= c[0]
        d = str(a)[-1]
        if c[0] == int(d):
            break
        c.append(int(d))
    e = b % len(c)
    if a == 0:
        print(10)
    elif e == 0:
        print(c[-1])
    else:
        print(c[e-1])
    
