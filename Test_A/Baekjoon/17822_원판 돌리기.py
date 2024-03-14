import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M, T = map(int, input().split())
arr = [deque(map(int, input().split())) for _ in range(N)]
for _ in range(T):
    # x의 배수인 원판을 d방향으로 k칸 회전
    # d: 0 시계방향 1 반시계방향
    x, d, k = map(int, input().split())

    # x의 배수인 원판만 선택
    for i in range(x-1, N, x):
        # d 방향으로 k칸 회전
        for _ in range(k):
            # 시계 방향
            if d == 0:
                arr[i].appendleft(arr[i].pop())
            # 반시계 방향
            else:
                arr[i].append(arr[i].popleft())

    # 회전 종료 후 점수 계산
    s = 0
    num = 0
    deleted = False
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                temp = arr[i][j]
                for d in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    ni = i + d[0]
                    nj = (j + d[1] + M) % M
                    if 0<=ni<N and temp == arr[ni][nj]:
                        arr[ni][nj] = 0
                        arr[i][j] = 0
                        deleted = True
        s += sum(arr[i])
        num += (M - arr[i].count(0))
    print('start')
    for i in range(N):
        print(arr[i])
    # 평균 계산 후 숫자 수정
    if not deleted:
        average = s / num
        for i in range(N):
            for j in range(M):
                if arr[i][j] and arr[i][j] > average:
                    arr[i][j] -= 1
                elif arr[i][j] and arr[i][j] < average:
                    arr[i][j] += 1
        print('not deleted')
        print(average)
        for i in range(N):
            print(arr[i])
ss = 0
for i in range(N):
    ss += sum(arr[i])
    print(arr[i])
print(ss)

