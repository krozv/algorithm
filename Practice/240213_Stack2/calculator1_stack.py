# calculator1 - stack
"""
수식문자열을 읽어서 피연산자는 바로 출력하고 연산자는 스택에 push하여 수식이 끝나면
스택의 남아있는 연산자를 모두 pop하여 출력하시오.
연산자는 사칙 연산만 사용하시오
"""

stack = [0]*100
top = -1
icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 안에서의 우선순위

fx = '(6+5*(2-8)/2)'
postfix = ''
for tk in fx:
    # 여는 괄호 push, or 연산자이고 top 원소보다 우선순위가 높으면 push
    if tk == '(' or (tk in '*/+-' and isp[stack[top]] < icp[tk]):
        # push
        top += 1
        stack[top] = tk
    elif tk in '*/+-' and isp[stack[top]] >= icp[tk]: # 연산자이고 top 원소보다 우선순위가 같거나 낮으면 pop
        # top 원소보다 우선순위가 낮을 때까지 pop
        while isp[stack[top]] >= icp[tk]:
            top -= 1
            postfix += stack[top+1]
        # push
        top += 1
        stack[top] = tk
    elif tk == ')':     # 닫는 괄호면, 여는 괄호를 만날 때까지 pop
        while stack[top] != '(':
            top -= 1    # pop
            postfix += stack[top+1]
        top -= 1    # 여는 괄호 pop 해서 버림
    else:   # 피연산자인 경우
        postfix += tk
print(postfix)
