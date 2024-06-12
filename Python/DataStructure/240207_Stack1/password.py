# Stack1. 비밀번호
"""
문제
N개의 정수 중 짝수는 몇 개인지 출력
조건
1. T 테스트케이스 1 <= T <= 10
2. N 주어진 정수 5 <= N <= 100000
"""
def push(item):
    # global 변수 top 선언
    global top
    top += 1
    # overflow 확인
    if top == -1:
        print('overflow')
    # item를 stack에 쌓는다
    else:
        stack[top] = item


def pop():
    # global 변수 top 선업
    global top
    # underflow 확인
    if top == -1:
        print('underflow')
    # 제거제거
    else:
        stack[top] = 0
        top -= 1
        # 어떻게 제거할 건지 고민중

import sys
sys.stdin = open('input.txt', 'r')
T = 10
for t in range(1, T+1):
    size, num_list = input().split()
    size = int(size)
    stack = [0] * size
    top = -1
    for i in range(size):
        # push
        if stack[top] != num_list[i]:
            push(num_list[i])
        # pop
        else:
            pop()
    password = ''
    for item in stack:
        if type(item) is str:
            password += item
    print(f'#{t} {password}')



