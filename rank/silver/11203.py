# 트리의 레벨과 L/R을 통한 이동으로 해당 노드의 값을 찾는 문제

V = list(input().split())
val = 0
for _ in range(int(V[0])+1):
    val += 2**_
now = 1
if len(V) == 1:
    print(val)
else:
    for i in V[1]:
        if i == 'L':
            now *= 2
        else:
            now = now*2 + 1
    print(val - now + 1)