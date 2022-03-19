S_lst = [64]
N = int(input())
while True:
    if sum(S_lst) == N:
        print(len(S_lst))
        break
    minV = S_lst.pop(0)//2

    if sum(S_lst) + minV >= N:
        S_lst.insert(0, minV)
    else:
        S_lst.insert(0, minV)
        S_lst.insert(0, minV)