word = input()
cro_lst = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
cnt = 0
for i in range(len(word)-1):
    a = word[i] + word[i+1]
    if a in cro_lst:
        cnt += 1
for i in range(len(word)-2):
    a = word[i] + word[i+1] + word[i+2]
    if a == 'dz=':
        cnt += 1
print(len(word) - cnt)