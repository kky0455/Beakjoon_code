num = int(input())
scores = list(map(int, input().split()))
max = max(scores)
new_scores = list()
for i in scores:
    new_scores.append((i / max) * 100)
print(sum(new_scores) / num)