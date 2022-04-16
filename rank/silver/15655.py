def find(idx):
    global ans
    # ans의 길이가 M과 같으면 리턴
    if len(ans) == M:
        print(*ans)
    # 다음 탐색을 진행하기위한 for문
    for i in range(idx+1, N):
        ans.append(arr[i])
        find(i)
        ans.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
# 오름차순 출력을 위해 정렬
arr.sort()
# for문으로 시작점 지정
for i in range(N):
    ans = [arr[i]]
    find(i)
