# 괄호 검사 직접해보기
def push(n):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = n


def pop():







top = -1
size = 10
stack = [0]*10  # 최대 10개 push