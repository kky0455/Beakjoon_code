def num(N):
    # 찾는 수가 소수리스트의 마지막 수보다 작으면 pass
    if lst[-1] > N:
        pass
    else:
        for i in range(lst[-1], N):
            for j in lst:
                is_num = True
                if i % j == 0:
                    # ARR[i] = 0
                    is_num = False
                    break
            if is_num == True and i not in lst:
                lst.append(i)

T = int(input())
# 소수 담기
lst = [2]
# 전체 수 리스트
# ARR = [1] * 10001
for tc in range(T):
    N = int(input())
    num(N)
    min_num = 10000000000
    h = N//2
    for i in range(h):
        if (h - i) in lst and (N - h + i) in lst:
            ans_x = h - i
            ans_y = N - h + i  
            break

    print(f'{ans_x} {ans_y}')
