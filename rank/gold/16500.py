# 주인공 : 저 혹시 면접용 정장 대여하고싶은데 대여 가능한가요?
# 취업센터 : 아 지금 모든 정장이 대여중이어서 일주일뒤에나 가능할거같은데요??
# 주인공 : 아 그래요? 당장 이틀뒤에 면접인데 어떡하죠??ㅠㅠ
# 취업센터 : 피트윈으로 빌려보시는건 어떠세요??
# 주인공 :  피트윈이요??

import sys
input = sys.stdin.readline

def find(idx):
    if idx == len(S):
        return True
    # if DP[idx]:
    #     return False
    for i in arr:
        if S[idx:idx + len(i)] == i:
            DP[idx:idx+len(i)] = [1] * len(i)
            if find(idx + len(i)):
                return True
    return False


S = input().rstrip('\n')
A = int(input())
arr = []
DP = [0] * len(S)
for _ in range(A):
    arr.append(input().rstrip('\n'))
for i in arr:
    if S[:len(i)] == i:
        DP[:len(i)] = [1] * len(i)
        if find(len(i)):
            print(1)
            exit()
print(0)