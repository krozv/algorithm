# 계산기2
"""
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14nnAaAFACFAYD
"""
# 문자열 -> 후위표기식 -> 계산
def postfix(f):
    """
    f: 문자로 이루어진 계산식
    """
    isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}  # isp가 낮을수록 stack 내에 오래 존재
    icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}  # icp가 높을수록 stack 안에 들어갈 확률 증가
    op = '(+-*/)'
    stk = []
    post = ''
    for c in f:
        # c가 연산자일 경우
        if c in op:
            # stk이 비어있을 경우
            if not stk:
                stk.append(c)
            else:
                # c가 )일 경우: (가 나올 때까지 pop
                if c == ')':
                    while stk[-1] != '(':
                        post += stk.pop()
                    # ( 뽑아서 버림
                    stk.pop()
                # isp[stk[-1]] < icp[c]: push
                elif isp[stk[-1]] < icp[c]:
                    stk.append(c)
                # isp[stk[-1]] >= icp[c] : 낮아질 때까지 pop 후 추가
                elif isp[stk[-1]] >= icp[c]:
                    while stk and isp[stk[-1]] >= icp[c]:
                        post += stk.pop()
                    stk.append(c)
        # c가 연산자가 아닐 경우
        else:
            post += c
    if stk:
        for i in range(len(stk)-1, -1, -1):
            post += stk[i]
    return post


import sys
sys.stdin = open('input1 (1).txt', 'r')

T = 10
for t in range(1, T+1):
    _ = input()
    f = input()
    f2 = postfix(f)
    stack = []
    for char in f2:
        if char.isdigit():
            stack.append(int(char))
        else:
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(b + a)
            elif char == '-':
                stack.append(b - a)
            elif char == '*':
                stack.append(b * a)
            else:
                stack.append(b // a)
    print(f'#{t} {stack[0]}')