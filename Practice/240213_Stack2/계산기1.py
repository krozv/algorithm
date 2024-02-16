# 계산기1
"""
문자열로 이루어진 게산식이 주어짐
후위 표기식으로 바꾸어 계산하는 프로그램 작성
조건
1. 연산자는 + 뿐임
2. 숫자는 0~9까지의 정수
"""
def calculator(expression: str) -> int:
    """
    expression: 문자열로 이루어진 표현식
    """
    output = 0
    for char in expression:
        # operator가 아닌 경우 -> 그냥 계속 합
        if char.isdigit():
            output += int(char)
        # operator인 경우 -> pass
    return output


import sys
sys.stdin = open('input.txt', 'r')
T = 10
for t in range(1, T+1):
    N = int(input())
    ex = input()
    print(f'#{t} {calculator(ex)}')