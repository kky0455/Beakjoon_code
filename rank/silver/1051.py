N, M = map(int, input().split())
lst = []
A = 1
for i in range(N):
    lst.append(list(map(int, input())))
for i in range(N):
    for j in range(M):
        V = lst[i][j]
        for k in range(1, M-j):
            if lst[i][j+k] == V and i+k < N:
                if lst[i+k][j] == V and lst[i+k][j+k] == V:
                    B = (k+1) * (k+1)
                    if A < B:
                        A = B
print(A)

                