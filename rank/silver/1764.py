import sys
input = sys.stdin.readline

h, s = map(int, input().split())
h_lst = []
result = []

for i in range(h):
    h_lst.append(input())
for i in range(s):
    a = input()
    if a in h_lst:
        result.append(a)


result.sort()
print(result)