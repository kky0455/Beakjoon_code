up, down, goal = map(int, input().split())

D = goal - up
climb = up - down

if up == goal:
    print(1)
elif (D/climb) == (D//climb):
    print((D//climb)+1)
else:
    print((D//climb)+2)