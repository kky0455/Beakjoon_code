N, K = map(int, input().split())
val = ''
# 주어진 N을 2진수로 변환하기
# 1은 물병의 개수며 각 인덱스(idx)는 2**(idx)를 나타냄
while N != 0:
    a, b = divmod(N, 2)
    val = val + str(b)
    N = a
lst = list(map(int, val))
# 만약 물병의 개수가 K보다 작거나 같다면 추가 구매 필요없음
if sum(lst) <= K:
    print(0)
# 아니라면 다음 반복문 진행
else:
    cnt = 0
    # 이진수의 인덱스를 올라가며 2개의 1을 찾는다
    # 그 두 인덱스의 값의 차이로 구매해야할 물의 양을 계산(물 1병당 1리터)
    # 계산이 끝난 후 인덱스의 값이 2가된 곳을 정리해준다
    # 계산 후 물병의 개수가 K개보다 작거나 같다면 문제 없음(작다면 물병을 합치는 과정을 안해서 물병 개수를 맞출 수 있음)
    while sum(lst) > K:
        move = []
        for i in range(len(lst)):
            if lst[i] == 1:
                move.append(i)
                lst[i] = 0
            if len(move) == 2:
                break
        cnt += 2**move[1] - 2**move[0]
        if len(lst) == move[1]+1:
            lst.append(1)
        else:
            lst[move[1]+1] += 1
        for i in range(len(lst)):
            if lst[i] == 2:
                lst[i] = 0
                if len(lst) == i+1:
                    lst.append(1)
                else:
                    lst[i+1] += 1
    print(cnt)