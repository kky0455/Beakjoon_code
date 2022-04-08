A = int(input())
arr = list(map(int, input().split()))
# 각 인덱스에 최대 증가수열을 저장
visited = [[] for _ in range(A)]
# 최소 경우의 수는 1이기 때문에 모든 인덱스에 1 저장
l_lst = [1] * A

for i in range(0, A):
    # 자신 전 인덱스까지 탐색 진행
    for j in range(0, i):
        # 현재 값보다 작지만 더 큰 증가수열을 가지고 있다면 visited에 저장된 배열을 deepcopy
        if arr[i] > arr[j] and len(visited[j]) + 1 > len(visited[i]):
            visited[i] = visited[j][::]
    # 탈출하면서 자기 자신의 값도 저장
    visited[i].append(arr[i])
    # l_lst에는 길이 저장
    l_lst[i] = len(visited[i])
# 길이가 가장 긴 증가 수열 저장
print(max(l_lst))
# 최대값을 가진 리스트의 인덱스를 가져와 언팩
print(*visited[l_lst.index(max(l_lst))])