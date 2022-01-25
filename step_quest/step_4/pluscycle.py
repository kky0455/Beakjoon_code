num = input()
cnt = 0 # 횟수
tmp = ''
int_num = 0 # 덧셈용
str_num = '00' # 문자용

if int(num) < 10 :
    original_num = '0' + num
else :
    original_num = num

while True:
    cnt += 1
    num = int(num)
    num = str(num)

    if int(num) < 10:
        tmp = '0' + num
    else:
        tmp = num
    if int(num)< 10:
        str_num = str_num[1] + num
    else :
        int_num = int(num[0]) + int(num[1])
        if int_num < 10:
            str_num = '0' + str(int_num)
        else:
            str_num = str(int_num)
    if int(num) < 10:
        num = num + str_num[1]
    else:
        num = num[1] + str_num[1]
    str_num = tmp
    if num == original_num:
        print(cnt)
        break

