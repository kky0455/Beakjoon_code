#2 3 4 5  6  7  8  9
#1 2 3 4  5  6  7  8
#1 3 6 10 15 21 28 36
#1 3/2 2 5/2 3 7/2
num = int(input())
n = 1
start = 0
cnt = 1
while True:
    a = num - start
    start += n
    if num <= start:
        break
    n += 1
    cnt += 1

if cnt % 2 == 1:
    print(f'{(cnt+1)-a}/{a}')
else:
    print(f'{a}/{(cnt+1)-a}')