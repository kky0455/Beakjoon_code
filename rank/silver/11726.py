n = int(input())
DP = [0, 1, 2]
for i in range(3, n+1):
    DP.append(DP[i-2] + DP[i-1])
print(DP[n] % 10007)