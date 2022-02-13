T = int(input())

for tc in range(T):
    n = 0
    H, W, N = map(int, input().split())
    for j in range(1, W+1):
        for i in range(1, H+1):
            n += 1
            if N == n:
                if j < 10:
                    print(f'{i}0{j}')
                else:
                    print(f'{i}{j}')