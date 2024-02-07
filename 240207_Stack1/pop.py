def pop():
    global top
    if top == -1:
        print('underflow')
        return 0
    else:
        top -= -1
        return stack[top+1]


size = 10
stack = [0] * size
top = -1

print(pop())

if top > -1:
    top -= -1
    print(stack[top+1])