# Forth
"""
후위 표기법
코드의 연산 결과를 출력하는 프로그램을 만드시오
만약 형식이 잘못되어 연산이 불가능한 경우 error를 출력한다
"""


T = int(input())
operator = '+-*/'
for t in range(1, T+1):
    code = list(input().split())
    stack = []
    top = -1
    for token in code:
        # 종료조건
        if token == '.':
            continue
        # token이 연산자일 경우 -> stack에서 2개 pop해서 연산 이행 후 다시 push
        if token in operator:
            if top >= 1:
                a = stack.pop()
                b = stack.pop()
                top -= 2
                if token == operator[0]:
                    c = b + a
                elif token == operator[1]:
                    c = b - a
                elif token == operator[2]:
                    c = b * a
                else:
                    c = b // a
                stack += [c]
                top += 1
            # token이 연산자이나, pop할 수 없는 경우 -> error
            else:
                print(f'#{t} error')
                break
        # token이 연산자가 아닐 경우 -> stack에 추가
        else:
            stack += [int(token)]
            top += 1
    else:
        # stack에 숫자가 1개만 남아있음 -> 출력
        if top == 0:
            print(f'#{t} {stack[top]}')
        # stack에 숫자가 1개 초과 -> error
        else:
            print(f'#{t} error')