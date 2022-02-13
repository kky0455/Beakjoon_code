import sys
import copy

table=[1, 1, 1, 1, 1, 1, 1, 1, 1]
for i in range(len(table)):
    if table[i] == 1 and i > 1:
        k=i*2
        while(k < len(table)):
            table[k]=0
            k+=i

