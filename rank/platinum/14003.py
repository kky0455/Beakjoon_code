# 골드와 플레는 다르다 ㅠㅠ 시간초과 발생....
A = int(input())
arr = list(map(int, input().split()))
# 최소 경우의 수는 1이기 때문에 모든 인덱스에 1 저장
visited = [[] for _ in range(A)]
l_lst = [1] * A
# 마지막의 경우의 수는 무조건 1, 끝에서 두번째 인덱스부터 탐색
for i in range(0, A):
    # 끝에서부터 자기 앞 인덱스까지 탐색
    for j in range(0, i):
        # 자기보다 더 작은 값을 만났을 때, 그 인덱스에 저장된 수 +1이 자신보다 크면 저장
        # 인덱스에 최대감소부분수열을 저장하기 때문
        if arr[i] > arr[j] and len(visited[j]) + 1 > len(visited[i]):
            visited[i] = visited[j][::]
    visited[i].append(arr[i])
    l_lst[i] = len(visited[i])
print(max(l_lst))
print(*visited[l_lst.index(max(l_lst))])
