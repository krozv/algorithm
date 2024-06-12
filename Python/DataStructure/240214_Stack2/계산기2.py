# 계산기2
"""
후위 표기식
연산자 +, *
피연산자 0~9
"""
def change_expression(expression):
    prior = {'+': 1, '*': 2}
    stk = [0] * length  # 연산자를 넣을 stack
    top = -1
    postfix = ''
    for tk in expression:
        # print(tk)
        # print('postfix:', postfix)
        # print(top, stk)
        # if len(stack) == 0 -> push
        if tk in operator:
            if top == -1:
                top += 1
                stk[top] = tk
            # if tk is operator and icp[stack[top]] < isp[tk] -> push
            elif prior[stk[top]] < prior[tk]:
                top += 1
                stk[top] = tk
            # elif tk is operator and icp[stack[top]] >= isp[tk] -> pop
            elif prior[stk[top]] >= prior[tk]:
                # print(prior[stk[top]])
                # while icp[stack[top]] >= isp[tk]:
                while top >= 0 and prior[stk[top]] >= prior[tk]:
                    # pop
                    postfix += stk[top]
                    stk[top] = 0
                    top -= 1
                top += 1
                stk[top] = tk

        # else not operator: -> 문자열에 삽입
        else:
            postfix += tk
    ## 반대로 꺼내야함
    if stk:
        for tk in stk:
            postfix += tk
    return postfix


import sys
sys.stdin = open('input.txt', 'r')
operator = '*+'
for t in range(1, 11):
    length = int(input())
    expression = input()
    print(change_expression(expression))