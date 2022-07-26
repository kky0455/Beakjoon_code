import math

N = int(input())
quest = list(map(int, input().split()))
numLst = [0] * (N+1)
fac = [0] * (N+1)
ans = []
if quest[0] == 1:
    num = N-1
    while quest[1] != 0 :
        val = math.factorial(num)
        quo, rem = divmod(quest[1], val)
        cnt = 0
        for i in range(1, N+1):
            if not numLst[i]:
                cnt += 1
                if rem > 0:
                    if quo+1 == cnt:
                        numLst[i] = 1
                        ans.append(i)
                        break
                elif rem == 0:
                    if quo == cnt:
                        numLst[i] = 1
                        ans.append(i)
                        break
        quest[1] %= val
        num -= 1
    for i in range(1, N+1):
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