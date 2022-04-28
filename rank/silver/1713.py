N = int(input())
stu = int(input())
# 사진틀의 역할
picture = []
# 학생번호를 인덱스로하는 리스트 생성, 투표수 저장
s_lst = [1000000000] * (stu+1)
pick = list(map(int, input().split()))
for i in pick:
    # 사진틀이 N개가 아니라면 추가
    if len(picture) < N:
        if s_lst[i] != 1000000000:
            s_lst[i] += 1
        else:
            picture.append(i)
            s_lst[i] = 1
    # 3인경우
    else:
        if s_lst[i] != 1000000000:
            s_lst[i] += 1
        else:
            minV = min(s_lst)
            for j in picture:
                if s_lst[j] == minV:
                    picture.remove(j)
                    s_lst[j] = 1000000000
                    picture.append(i)
                    s_lst[i] = 1
                    break
for i in range(1, stu+1):
    if s_lst[i] != 1000000000:
        print(i, end=' ')
print()