# 6일차 - 계산기1
"""
후위 표기식으로 바꾸어 계산하는 프로그램
연산자: +
피연산자: 0~9 정수
"""
import sys
sys.stdin = open('input.txt', 'r')
T = 10
for t in range(1, T+1):
    length = int(input())
    expression = input()
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(char)
        else:
            if len(stack) < 2:
                print(stack[0])
                break
            a = stack.pop()
            b = stack.pop()
            stack.append(int(a)+int(b))

