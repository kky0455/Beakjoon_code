a, b, c = map(int, input().split())

earn = c - b
if earn <= 0:
    print(-1)
else:
    print((a//earn) + 1)
