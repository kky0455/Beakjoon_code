def num(ARR):
    for i in range(2, 1001):
        if ARR[i] == 1:
            n = 2*i
            while n <= 1000:
                ARR[n] = 0
                n += i

N = int(input())
ARR = [1] * 1001
lst = list(map(int, input().split()))
num(ARR)
l = []
for i in range(2, 1001):
    if ARR[i] == 1:
        l.append(i)
cnt = 0
for i in lst:
    if i in l:
        cnt += 1
print(cnt)