T = int(input())

for tc in range(1, T+1):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = (x1-x2)**2 + (y1-y2)**2
    r3 = (r1-r2)**2
    r4 = (r1+r2)**2
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif d < r4 and d > r3:
        print(2)
    elif d == r4:
        print(1)
    elif d == r3 and d != 0:
        print(1)
    elif d < r3:
        print(0)
    elif d > r4:
        print(0)