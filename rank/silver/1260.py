import sys
input = sys.stdin.readline

# dfs와 bfs기본 복습
# dfs는 재귀가 최고인가???

def dfs():
    visited = [0] * (N+1)
    stack = [V]
    while stack:
        val = stack.pop()
        if not visited[val]:
            visited[val] = 1
            print(val, end=' ')
            for i in G[val][::-1]:
                if not visited[i]:
                    stack.append(i)
    print()

def bfs():
    visited = [0] * (N+1)
    q = [V]
    visited[V] = 1
    while q:
        val = q.pop(0)
        print(val, end=' ')
        for i in G[val]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
    print()

N, M, V = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for _ in G:
    _.sort()
dfs()
bfs()