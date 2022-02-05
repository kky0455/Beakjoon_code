num = list()
result = 0
for i in range(10):
    a = int(input())
    b = a % 42
    num.append(b)
for i in range(42):
    if num.count(i) > 0 :
        result += 1
print(result)



    