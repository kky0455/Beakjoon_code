N, M = map(int, input().split())
rate = list(map(float, input().split()))
good = [0] * (N+1)
bad = [0] * (N+1)
if M == 0:
    good[0] = 1.0
else:
    bad[0] = 1.0

for i in range(1, N+1):
    good[i] = good[i-1] * rate[0] + bad[i-1] * rate[2]
    bad[i] = good[i-1] * rate[1] + bad[i-1] * rate[3]


print(int(round(good[N] * 1000)))
print(int(round(bad[N] * 1000)))