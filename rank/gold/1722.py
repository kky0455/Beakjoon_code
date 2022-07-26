import math

N = int(input())
quest = list(map(int, input().split()))
numLst = [0] * (N+1)
fac = [0] * (N+1)
ans = []
if quest[0] == 1:
    num = N-1
    ans = []
    while quest[1] > 0:
        cnt = 0
        que, rem = divmod(quest[1], math.factorial(num))
        for i in range(1, N+1):
            if not numLst[i]:
                cnt += 1
                if rem > 0 :
                    if cnt == que+1:
                        numLst[i] = 1
                        ans.append(i)
                        break
                else:
                    if cnt == que:
                        numLst[i] = 1
                        ans.append(i)
                        break
        quest[1] = rem
        num -= 1
    for i in range(N, 0, -1):
        if not numLst[i]:
            ans.append(i)
    print(*ans)
else:
    num = 1
    ans = 1
    while num < N+1:
        cnt = 0
        for i in range(1, N+1):
            if not numLst[i]:
                if quest[num] != i:
                    cnt += 1
                else:
                    ans += cnt * math.factorial(N-num)
                    numLst[i] = 1
                    break
        num += 1
    print(ans)