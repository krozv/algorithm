# 10845. 큐
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    command = input().split()
    # push 연산
    if len(command) == 2:
        queue.append(int(command[1]))
        continue
    match (command[0]):
        case ('pop'):
            if queue:
                print(queue[0])
                queue = queue[1:]
            else:
                print(-1)
        case ('size'):
            print(len(queue))
        case ('empty'):
            print(int(len(queue)==0))
        case ('front'):
            if queue:
                print(queue[0])
            else:
                print(-1)
        case ('back'):
            if queue:
                print(queue[-1])
            else:
                print(-1)