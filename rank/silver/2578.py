def row_check(ARR):
    cnt = 0
    for i in ARR:
        if sum(i) == 0:
            cnt += 1
    return cnt

def col_check(ARR):
    cnt = 0

    for i in range(5):
        check = 0
        for j in range(5):
            if ARR[j][i] == 0:
                check += 1
        if check == 5:
            cnt += 1
    return cnt
    
def cro_check(ARR):
    cnt = 0
    if ARR[2][2] == 0:
        sum1 = ARR[2][2]
        sum2 = ARR[2][2]
        for i in range(1, 3):
            sum1 += ARR[2+i][2+i]
            sum1 += ARR[2-i][2-i]
            sum2 += ARR[2-i][2+i]
            sum2 += ARR[2+i][2-i]
        if sum1 == 0:
            cnt += 1
        if sum2 == 0:
            cnt += 1
    return cnt

ARR = [list(map(int, input().split())) for _ in range(5)]
ARR2 = [list(map(int, input().split())) for _ in range(5)]

for h in range(2):
    for k in ARR2[h]:
        for i in range(5):
            for j in range(5):
                if ARR[i][j] == k:
                    ARR[i][j] = 0

cnt = 10
for h in range(2, 5):
    for k in ARR2[h]:
        for i in ARR:
            ans = 0
            for j in range(5):
                if i[j] == k:
                    i[j] = 0
                    cnt += 1
                    ans += row_check(ARR)
                    ans += col_check(ARR)
                    ans += cro_check(ARR)
                if ans >= 3:
                    break
            if ans >= 3:
                    break
        if ans >= 3:
                    break
    if ans >= 3:
                    break
print(cnt)