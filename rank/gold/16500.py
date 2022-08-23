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