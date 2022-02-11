#1 7 19 37 61...
room = int(input())
range = 1
n = 0
floor = 1
while True:
    floor += 6*n
    if room <= floor:
        print(range)
        break
    n += 1
    range += 1
