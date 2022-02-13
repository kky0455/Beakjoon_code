h, m = map(int,input().split())
p = int(input())
m = m+p


if m > 59:
    h += int(m / 60)
    m = m % 60
    
if h > 23:
    h -= 24


print(f'{h} {m}')
