# 현주의 박스 바꾸기
'''
N 상자 개수 - 처음엔 0이라고 적힘
Q 변경 횟수 - 일정 범위의 연속한 상자를 동일한 숫자로 변경
i (1 <= i <= Q)번째 작업 L~R상자까지 값을 i로 변경
N개의 상자에 적힌 값 출력
'''
import sys
sys.stdin = open('input_box.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, Q = map(int, input().split())   # 1 <= N, Q <= 1000
    boxes = [0] * N
    for q in range(1, Q+1):
        L, R = map(int, input().split())    # 1<=L<=R<=N
        for i in range(L, R+1):
            boxes[i-1] = q

    print(f'#{t}', end=' ')
    print(*boxes)



