# 괄호검사
"""
괄호가 제대로 짝을 이뤘는지 검사
정상1, 아니면0
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    s = input()
    stk = []
    for char in s:
        if char in '{}()':
            if char in '{(':
                stk.append(char)
            else:
                if char == ')':
                    if stk and stk[-1] == '(':
                        stk.pop()
                    else:
                        print(f'#{t} 0')
                        break
                else:
                    if stk and stk[-1] == '{':
                        stk.pop()
                    else:
                        print(f'#{t} 0')
                        break
    else:
        if not stk:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
