import heapq
import sys
input = sys.stdin.readline

def dijk():
    D = [-1000000000000000000] * N
    q = []
    D[S] = earn[S]
    heapq.heappush(q, (earn[S], S))
    visited = [0] * N
    visited[S] = 1
    while q:
        dis, now = heapq.heappop(q)
        for e, d in G[now]:
            if D[e] < dis + earn[e] - d:
                D[e] = dis + earn[e] - d
                visited[e] += 1
                if visited[e] == 1:
                    heapq.heappush(q, (D[e], e))
    if D[E] == -1000000000000000000:
        return print('gg')

    loop_lst = []
    for i in range(len(visited)):
        if visited[i] > 1:
            loop_lst.append(i)
    if loop_lst:
        for val in loop_lst:
            V = [-1000000000000000000] * N
            V[val] = 0
            heapq.heappush(q, (V[val], val))
            visited = [0] * N
            while q:
                dis, now = heapq.heappop(q)
                for e, d in G[now]:
                    if V[e] < dis + earn[e] - d:
                        V[e] = dis + earn[e] - d
                        visited[e] += 1
                        if visited[e] == 1:
                            heapq.heappush(q, (V[e], e))
            if visited[E] > 0:
                return print('Gee')
    print(D[E])


N, S, E, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    s, e, d = map(int, input().split())
    G[s].append((e, d))
earn = list(map(int, input().split()))
dijk()