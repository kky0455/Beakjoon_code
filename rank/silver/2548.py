N = int(input())
lst = list(map(int, input().split()))
lst.sort()
result = 10000000000
num = 20000
for i in lst:
    val = 0
    for j in lst:
        val += abs(i-j)
        if val > result:
            break
    if val < result:
        result = val
        num = i
    elif val == result and num > i:
        num = i

print(num)



