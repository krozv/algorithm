# 계산기1
"""
문자열 -> 후위표기식으로 변경 -> 계산
"""
def postfix(expression):
    isp = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
    icp = {'(': 3, '+': 1, '-': 1, '*': 2, '/': 2}
    op = '(+-*/)'
    stk = []
    f2 = ''
    for c in f:
        # c가 연산자일 경우
        if c in op:
            # stk이 존재하지 않을 때, 연산자 삽입
            if not stk:
                stk.append(c)
            else:
                # pop: c가 ) 인 경우, ( 가 나올때까지 pop
                if c == ')':
                    while stk[-1] != '(':
                        f2 += stk.pop()
                    stk.pop()
                # push: 연산자의 우선순위가 isp < icp 인 경우
                elif isp[stk[-1]] < icp[c]:
                    stk.append(c)
                # pop: 연산자의 우선순위가 isp >= icp인 경우 ->
                elif isp[stk[-1]] >= icp[c]:
                    # isp < icp가 될 때까지 pop
                    while stk and isp[stk[-1]] >= icp[c]:
                        f2 += stk.pop()
                    # pop 완료 후 append
                    stk.append(c)
        # c가 연산자가 아닐 경우
        else:
            f2 += c
    if stk:
        for s in range(len(stk) - 1, -1, -1):
            f2 += stk[s]
    return f2


import sys
sys.stdin = open('input1 (1).txt', 'r')
fx = '(6+5*(2-8)/2)'

T = 10
for t in range(1, T+1):
    _ = input()
    f = input()
    # 문자열 -> 후위표기식으로 변경
    post = postfix(f)
    # 후위표기식 -> 계산
    stack = []
    for c in post:
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
            else:
                stack.append(b // a)
    print(f'#{t} {stack[0]}')