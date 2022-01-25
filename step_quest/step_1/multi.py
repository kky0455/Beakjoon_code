a = int(input())
b = input()
cal = list()

for i in b:
    c = int(i) * a
    cal.append(c)

multi1 = cal[-1]
print(multi1)
multi2 = cal[1]
print(multi2)
multi3 = cal[0]
print(multi3)
multi4 = multi1 + multi2*10 + multi3 *100
print(multi4)