# 오목 판정
"""

"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    test = False
    for i in range(N):
        for j in range(N):
            # 방향 탐색 시작
            if not test and arr[i][j] == 'o':
                delta = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

                for k in range(8):
                    ni = i
                    nj = j
                    cnt = 1

                    while not test:
                        ni += delta[k][0]
                        nj += delta[k][1]

                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                            cnt += 1

                            if cnt == 5:
                                test = True
                                break
                        else:
                            break
    if test:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')