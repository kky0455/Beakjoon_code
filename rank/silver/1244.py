T = int(input())
Switch = [0] + list(map(int, input().split()))
Stu_Num = int(input())

for i in range(Stu_Num):
    S, N = map(int, input().split())
    if S == 1:
        for j in range(1, T+1):
            if (j) % N == 0:
                if Switch[j] == 0:
                    Switch[j] = 1
                else:
                    Switch[j] = 0
    if S == 2:
        if N == 1 or N == T:
            if Switch[N] == 1:
                Switch[N] = 0
            else:
                Switch[N] = 1
        else:
            for j in range(T-2, -1, -1):
                cnt = 0
                if j == 0:
                    if Switch[N] == 0:
                        Switch[N] = 1
                    else:
                        Switch[N] = 0
                elif 1 <= N-j and N+j <= T:
                    for k in range(1, j+1):
                        if Switch[N-k] != Switch[N+k]:
                            break
                        else:
                            cnt += 1
                    if cnt == j:
                        for l in range(2*j+1):
                            if Switch[N-k+l] == 0:
                                Switch[N-k+l] = 1
                            else:
                                Switch[N-k+l] = 0
                        break
N = int(len(Switch)+1/20)

for i in range(N):
    print(*Switch[1+20*i:21+20*i])
