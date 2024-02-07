# 4일차 - 괄호검사
def push(n):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = n


def pop():
    global top
    if top == -1:
        return 0
    else:
        top -= 1
        return 1




T = int(input())
for t in range(1, T+1):
    string = input()
    top = -1
    size = len(string)
    stack = [0]*size
    for char in string:
        if char in '{(':
            push(char)
        elif char in '})':
            if [stack[top], char] in [['(', ')'], ['{', '}']]:
                if pop():
                    stack.pop(top+1)
            else:
                print(f'#{t} 0')
                break
    else:
        if top == -1:
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')


