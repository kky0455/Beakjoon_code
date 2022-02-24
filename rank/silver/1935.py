dic = {}
Num = []
N = int(input())
S = input()
for i in range(N):
    dic[chr(65+i)] = int(input())

for i in S:
    if i == '+':
        Num.append(Num.pop() + Num.pop())
    elif i == '-':
        a = Num.pop()
        b = Num.pop()
        Num.append(b - a)
    elif i == '*':
        Num.append(Num.pop() * Num.pop())
    elif i == '/':
        a = Num.pop()
        b = Num.pop()
        Num.append(b / a)
    else:
        Num.append(dic[i])
print("%.2f" %Num[0])