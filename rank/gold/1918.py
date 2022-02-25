in_dic = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 3}
out_dic = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0}
Op_lst = ['+', '-', '*', '/', '(', ')']
S = input()
Num = []
Op = []

for i in S:
    if i in Op_lst:
        if not Op:
            Op.append(i)
        elif i == ')':
            while Op[-1] != '(':
                Num.append(Op.pop())
            Op.pop()
        elif out_dic[Op[-1]] < in_dic[i]:
            Op.append(i)
        else:
            while Op and out_dic[Op[-1]] >= in_dic[i]:
                Num.append(Op.pop())
            Op.append(i)
    else:
        Num.append(i)
while Op:
    Num.append(Op.pop())
for i in Num:
    print(i, end='')