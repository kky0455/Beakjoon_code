n = int(input())
cnt = 0
while cnt < n:
    ox = input()
    up = 1
    total = 0
    for i in ox:
        if i == 'O':
            total += up
            up += 1
        else:
            up = 1
    print(total)
    cnt += 1