import heapq
import sys
input = sys.stdin.readline

def bell():
    D = [-1000000000] * N
    D[S] = earn[S]
    for i in range(N+1):
        if i == N and D[E] == -1000000000:
            return print('gg')
        for j in range(N):
            if D[j] == -1000000000:
                continue
            for e, d in G[j]:
                if D[e] < D[j] + earn[e] - d:
                    D[e] = D[j] + earn[e] - d
                    if i == N:
                        visited = [0] * N
                        q = []
                        heapq.heappush(q, e)
                        while q:
                            now = heapq.heappop(q)
                            if now == E:
                                return print('Gee')
                            visited[now] = 1
                            for e, d in G[now]:
                                if visited[e] == 0:
                                    heapq.heappush(q, e)
    return print(D[E])

N, S, E, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    s, e, d = map(int, input().split())
    G[s].append((e, d))
earn = list(map(int, input().split()))
bell()