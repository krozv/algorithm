def push(item, size):
    global top
    top += 1
    if top == size:     # 오버플로우 확인 코드(디버깅용 코드)
        print('overflow!')
    else:
        stack[top] = item


size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20