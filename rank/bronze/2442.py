N = int(input())
for i in range(1,N+1):
    star = ' ' * (N-i) + '*' * ((2*i)-1)
    print(star)