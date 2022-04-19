N = int(input())
# 학생별 학년마다 어느 반에 속해있는데 3단 배열 생성
arr = [[[] for _ in range(10)] for _ in range(6)]
# 같은 반을 한 친구들의 정보를 넣기 위한 리스트 생성
score = [[] for _ in range(N+1)]
# 1번 학생부터 학년별 반 정보를 받아 arr리스트에 저장
stu = 1
for i in range(N):
    grade = 1
    lst = list(map(int, input().split()))
    for j in lst:
        arr[grade][j].append(stu)
        grade += 1
    stu += 1
# 1~5학년, 1~9반까지 탐색 진행
# 만약 리스트의 길이가 2이상일 때 score의 해당 학생 인덱스에 같은 반 친구 정보 입력
for i in range(1, 6):
    for j in range(1, 10):
        if len(arr[i][j]) >= 2:
            for k in range(len(arr[i][j])):
                for l in arr[i][j]:
                    if arr[i][j][k] != l and l not in score[arr[i][j][k]]:
                        score[arr[i][j][k]].append(l)

# score리스트의 길이를 탐색하며 최대value를 가진 학생번호 출력
maxV = 0
ans = 1
for i in range(1, len(score)):
    if len(score[i]) > maxV:
        maxV = len(score[i])
        ans = i
print(ans)