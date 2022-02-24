x, y, w, h = map(int, input().split())
Min_val = 1111
if x > w - x:
    val = w - x
elif x < w - x:
    val = x
else:
    val = x

if Min_val > val:
    Min_val = val

if y > h - y:
    val = h - y
elif y < h - y:
    val = y
else:
    val = y

if Min_val > val:
    Min_val = val

print(Min_val)