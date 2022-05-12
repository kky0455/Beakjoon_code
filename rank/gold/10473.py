import math
import heapq
import sys
input = sys.stdin.readline

def dijk():
    D = [0] * C
    q = []
    for i in range(len(C_lst)):
        nx = s_x - C_lst[i][0]
        ny = s_y - C_lst[i][1]
        d = math.sqrt(nx**2 + ny**2) / 5
        D[i] = d
        heapq.heappush(q, (D[i], C_lst[i][0], C_lst[i][1]))
    # print(q)
    
    while q:
        dis, x, y = heapq.heappop(q)
        for i in range(len(C_lst)):
            nx = x - C_lst[i][0]
            ny = y - C_lst[i][1]
            if nx != 0 and ny != 0:
                d = math.sqrt(nx**2 + ny**2)
                if d > 25.0 and D[i] > abs(50-d) / 5 + 2 + dis:
                    D[i] = abs(50-d) / 5 + 2 +dis
                    heapq.heappush(q, (D[i], C_lst[i][0], C_lst[i][1]))
                elif D[i] > d / 5 + dis:
                    D[i] = d / 5 + dis
                    heapq.heappush(q, (D[i], C_lst[i][0], C_lst[i][1]))
    for i in range(len(C_lst)):
        nx = e_x - C_lst[i][0]
        ny = e_y - C_lst[i][1]
        d = math.sqrt(nx**2 + ny**2) / 5
        D[i] += d
    print(D)

C_lst = []
s_x, s_y = map(float, input().split())
e_x, e_y = map(float, input().split())
C = int(input())
for _ in range(C):
    x, y = map(float, input().split())
    C_lst.append((x, y))
dijk()