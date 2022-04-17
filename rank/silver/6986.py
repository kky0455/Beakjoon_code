# 부동소수점을 고려해야하는 문제!
N, K = map(int, input().split())
arr = [float(input()) for _ in range(N)]
arr.sort()
a = sum(arr[K:N-K])/(N-2*K) + 0.00000001
for i in range(K):
    arr[i] = arr[K]
    arr[-i-1] = arr[-K-1]
b = sum(arr)/N + 0.00000001
print('{:.2f}'.format(a))
print('{:.2f}'.format(b))