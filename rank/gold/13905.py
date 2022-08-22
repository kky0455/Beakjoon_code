import sys
input = sys.stdin.readline
import heapq

def dijk(start):
    D = [0] * (N+1)
    D[start] = 10000000
    q = []
    heapq.heappush(q, (start, D[start]))
    while q:
        node, val = heapq.heappop(q)
        if D[node] > val:
            continue
        for e, k in G[node]:
            if val < k:
                v = val
            elif val > k:
                v = k
            if D[e] 



N, M = map(int, input().split())
s, e = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    h1, h2, k = map(int, input().split())
    G[h1].append((h2, k))
    G[h2].append((h1, k))
dijk(s)