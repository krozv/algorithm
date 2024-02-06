# 4861. 회문
"""
팰린드롬
NxN 글자판에서 길이가 M인 회문을 찾아 출력
조건1. 회문은 1개 존재
조건2. 가로 or 세로
## fail 4개 ##
"""
import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())    # 1 <= T <= 50
for t in range(1, T+1):
    N, M = map(int, input().split())    # 10<=N<=100, 5<=M<=N
    arr = [list(input()) for _ in range(N)]
    # 가로 탐색
    for i in range(N):
        for j in range(N-M+1):
            start = j
            end = j+M-1
            while start < end:
                if arr[i][start] != arr[i][end]:
                    break
                else:
                    start += 1
                    end -= 1
            if start >= end:
                print(f'#{t}', ''.join(arr[i][j:j+M]))


    # 세로 탐색
    for i in range(N):
        for j in range(N-M+1):
            start = j
            end = j+M-1
            while start < end:
                if arr[start][i] != arr[end][i]:
                    break
                else:
                    start += 1
                    end -= 1
            if start >= end:
                print(f'#{t}', end=' ')
                for k in range(j, j+M):
                    print(arr[k][i], end='')
                print()