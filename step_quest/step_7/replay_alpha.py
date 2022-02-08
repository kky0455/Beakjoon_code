n = int(input())
cnt = 0
while cnt < n:
    mul, *string = input()
    for i in range(1,len(string)):
        print((string[i])*int(mul), end='')
    print('')
    cnt += 1 