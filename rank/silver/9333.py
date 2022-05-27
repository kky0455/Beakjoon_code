# 구현은 다 한거같은데 의문이 생기는 문제...
# 뭐가 잘못된거지???
T = int(input())
for _ in range(T):
    R, B, M = map(float, input().split())
    B *= 100
    M *= 100
    m = 0
    while True:
        m += 1
        if m >= 1200:
            print('impossible')
            break
        q, r = divmod(R*B, 100)
        if r/100 >= 0.5:
            q += 1
        B = B + q - M
        if B <= 0:
            print(m)
            break