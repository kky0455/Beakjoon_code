N = int(input())
n = int(input())
answer = '99'
len_N = len(str(N))
for i in range(0, 101):
    if N % n == 0 and int(answer) > int(str(N)[len_N-2:len_N]):
        answer = str(N)[len_N-2:len_N]
    N += 1
    if str(N)[len_N-2:len_N] == '00':
        N -= 100
print(answer)