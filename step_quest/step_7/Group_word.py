T = int(input())
cnt = 0
for tc in range(T):
    word = input()
    set_word = set(word)
    set_check = set()
    n = 0
    for i in set_word:
        if i in set_check:
            pass
        else:
            set_check.add(i)
            group = list()
            for j in range(len(word)):
                if i == word[j]:
                    group.append(j)
            if (group[-1] - group[0]) == (len(group)-1):
                n += 1
    if n == len(set_word):
        cnt += 1
print(cnt)