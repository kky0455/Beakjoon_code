N = int(input())
lst = list(map(int, input().split()))
a, b = map(int,input().split())
cnt = 0
for i in lst:
    i -= a
    cnt += 1
    if i > 0:
        if i % b == 0:
            cnt += i // b
        else:
            cnt += i//b + 1
print(cnt)