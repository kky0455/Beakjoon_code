from collections import deque
import sys
input = sys.stdin.readline

def dijk():
    D = [1000000000] * N
    D[0] = 0
    q = deque([0])
    while q:
        b, t = q.popleft()
        for i in range(N):
            if not visited[i] and D[i] > t + D[] and G[V][i]:
                D[i] = G[V][i] + D[V]
        maxV = 1000000000
        nextV = -1
        for i in range(N):
            if not visited[i] and D[i] < maxV:
                nextV = i
                maxV = D[i]
        q.append(nextV)
    return D[-1]

N, M = map(int, input().split())
visited = list(map(int, input().split()))
visited[N-1] = 0
lenV = N - visited.count(1)
G = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    G[a].append((b, t))
a = dijk()
if a == 1000000000:
    print(-1)
else:
    print(a)

# G를 1차원 배열
# deque를 그냥 q