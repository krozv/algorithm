# 암호생성기
"""
원형큐로 풀어봐야겠다
"""
import sys
sys.stdin = open('input (2).txt', 'r')
for t in range(1, 11):
    _ = input()
    num_list = list(map(int, input().split()))
    # 원형큐 생성
    front = 0
    rear = 1
    q = [0] + num_list     # password는 8자리니까 + front 1자리
    i = 1
    while True:
        if i == 6:
            i = 1
        if q[rear] - i > 0:
            q[front] = q[rear] - i
            q[rear] = 0
            i += 1
            front = rear
            rear = (rear+1) % 9
        else:
            q[front] = 0
            q[rear] = 0
            i += 1
            front = rear
            break
    password = list(map(str, q[front+1:]+q[:front]))
    print(f'#{t} {" ".join(password)}')