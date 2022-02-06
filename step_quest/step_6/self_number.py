num = list()
n = 1
start = 1
while start <= 10000:
    if start in num:
        pass
    else:
        print(start)
    if start < 10:
        start *= 2
        num.append(start)
    else:
        for i in str(start):
            start += int(i)
        num.append(start)
    n += 1
    start = n
