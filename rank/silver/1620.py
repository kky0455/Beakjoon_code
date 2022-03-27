import sys
input = sys.stdin.readline
dic = {}
N, M = map(int, input().split())
for i in range(N):
    dic[str(i+1)] = input().strip()
    dic[dic[str(i+1)]] = str(i+1)
for i in range(M):
    print(dic[input().strip()])