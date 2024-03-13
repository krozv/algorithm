# Forth
"""
후위 표기법
숫자를 스택에 넣고 연산자 만나면 연산
연산 불가할 경우 error 출력
"""
import sys
sys.stdin = open('input1 (1).txt', 'r')
T = int(input())
for t in range(1, T+1):
    arr = input().split()
    stk = []
    case = True
    for char in arr:
        if char == '.':
            break
        if char.isdigit():
            stk.append(int(char))
        else:
            if len(stk) > 1:
                a = stk.pop()
                b = stk.pop()
                if char == '+':
                    stk.append(b + a)
                elif char == '-':
                    stk.append(b - a)
                elif char == '*':
                    stk.append(b * a)
                else:
                    stk.append(b // a)
            else:
                case = False
                break
    if len(stk) == 1 and case:
        print(f'#{t} {stk[0]}')
    else:
        print(f'#{t} error')