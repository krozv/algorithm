# 반복문자 지우기
"""
문자열 S에서 반복문 문자 삭제
연결에 의해 또 반복문자가 생기면 다시 지움
남은 문자열의 길이 출력
"""
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(1, T+1):
    s = input()
    stk = [0] * 1000
    top = -1
    for char in s:
        if top < 0:
            top += 1
            stk[top] = char
        else:
            top += 1
            stk[top] = char

            while top > 0 and stk[top] == stk[top-1]:
                stk[top] = 0
                stk[top-1] = 0
                top -= 2
    l = 0
    for s in stk:
        if type(s) is str:
            l += 1
    print(f'#{t} {l}')
