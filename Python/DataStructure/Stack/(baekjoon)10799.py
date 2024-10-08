# 10799. 쇠막대기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

string = list(input())
stack = []
prev = ''
cnt = 0
for char in string:
    # prev == ( and char == ) : 레이저
    if prev == '(' and char == ')':
        # stack 에서 pop
        stack.pop()
        # 남은 stack 길이만큼 cnt 증가
        cnt += len(stack)
    # prev == ) and char == ) : 조각 꺼내기
    if prev == ')' and char == ')':
        # stack 에서 pop
        stack.pop()
        cnt += 1
    # char == ( : 조각 넣기
    if char == '(':
        # stack에 append
        stack.append(char)
    prev = char
print(cnt)