play = int(input())
n = 0
while n < play:
    cnt = 0
    stu, *sco = map(int, input().split())
    avg = sum(sco) / stu
    for i in sco:
        if i > avg:
            cnt += 1
    ratio = cnt/stu * 100
    # print('{}%'.format(cnt/stu * 100,'.3f')) 
    print('{:.3f}%'.format(ratio))
    n += 1   
