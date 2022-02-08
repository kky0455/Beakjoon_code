# a = 97, z = 122
# A = 65, Z = 90
from itertools import count

a = input()
num = list()
for i in range(97, 123):
    cnt = 0
    b = chr(int(i))
    cnt += a.count(b)
    c = b.upper()
    cnt += a.count(c)
    num.append(cnt)
if num.count(max(num)) > 1:
    print('?')
else:
    print(chr(int(num.index(max(num))+65)))