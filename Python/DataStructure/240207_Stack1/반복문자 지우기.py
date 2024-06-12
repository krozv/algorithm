# 4일차 - 반복문자 지우기
'''
조건1. 반복되면 문자쌍(2개)을 지움
조건2. 지운 후에도 반복되면 또 지움
'''
# stack에 하나씩 쌓아 올림
def push(n):
    """
    n: stack에 쌓을 문자 or 숫자
    """
    global top
    top += 1
    # stack overflow 확인
    if top == size:
        print('overflow')
    # stack 쌓기
    else:
        stack[top] = n


# stack에 쌓은 것 하나씩 제거
def pop():
    # global 변수 선언
    global top

    # stack underflow 확인
    if top == -1:
        print('underflow')
        return 0
    # stack 제거 -> method pop 사용 안하는 버전
    else:
        top -= 1
        stack[top + 1] = 0
        return 1    # 현재 스택에 존재하는 item 을 꺼내서 조건과 비교할 예정


import sys
sys.stdin = open('input1 (6).txt', 'r')

T = int(input())
for t in range(1, T+1):
    string = input()
    size = len(string)
    stack = [0] * size
    top = -1
    for item in string:
        # item 넣기 위한 조건 확인
        if top == -1:
            push(item)
        else:
            if stack[top] != item:
                push(item)
            else:
                pop()
    length = 0
    for item in stack:
        if type(item) is str:
            length += 1
    print(f'#{t} {length}')