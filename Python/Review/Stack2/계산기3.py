# 계산기3
"""
괄호 포함 후위 표기식 변경 -> 계산
"""
def postfix(f1):
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    stk = []
    op = '(+-*/)'
    f2 = ''
    for char in f1:
        if char in op:
            if not stk:
                stk.append(char)
            else:
                # char == ')'
                if char == ')':
                    while stk[-1] != '(':
                        f2 += stk.pop()
                    stk.pop()
                # isp[stk[-1]] < icp[char]: push
                elif isp[stk[-1]] < icp[char]:
                    stk.append(char)
                # isp[stk[-1]] >= icp[char]: 낮아질때까지 pop 후 push
                elif isp[stk[-1]] >= icp[char]:
                    while stk and isp[stk[-1]] >= icp[char]:
                        f2 += stk.pop()
                    stk.append(char)
        else:
            f2 += char
    if stk:
        for i in range(len(stk)-1, -1, -1):
            f2 += stk[i]
    return f2


import sys
sys.stdin = open('input1 (1).txt', 'r')
T = 10
for t in range(1, T+1):
    _ = input()
    f = input()
    stack = []
    for c in postfix(f):
        if c.isdigit():
            stack.append(int(c))
        else:
            a = stack.pop()
            b = stack.pop()
            if c == '+':
                stack.append(b + a)
            elif c == '-':
                stack.append(b - a)
            elif c == '*':
                stack.append(b * a)
    print(f'#{t} {stack[0]}')