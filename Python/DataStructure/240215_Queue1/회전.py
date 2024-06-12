# 회전
import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    # 큐 생성
    q = num_list
    front = 0
    # 삽입 및 삭제
    for _ in range(M):
        front = (front + 1) % N
    print(f'#{t} {q[front]}')
