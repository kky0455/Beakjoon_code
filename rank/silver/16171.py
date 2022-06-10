# 문자열만 선택하여 원하는 키워드가 들어있는지 확인하는 문제
# isdigit을 활용해 숫자를 제외한 문자열을 생성한 후 판단

word = list(input())
key = input()
f_word = ''
idx = []
for i in word:
    if not i.isdigit():
        f_word += i

if key in f_word:
    print(1)
else:
    print(0)
