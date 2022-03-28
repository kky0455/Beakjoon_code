N = int(input())
lst = list(map(int, input().split()))
lst.sort()
lst.insert(0, 1)
lst.append(20000)
result = 100000000000
num = 20001
for i in range(N+1):
    for j in range(lst[i], lst[i+1]):
        val = 0
        for k in lst:
            val += abs(k-j)
            if val > result:
                break
        if val < result:
            result = val
            num = j
        elif val == result and num > j:
            num = j

print(num)



