# 4836. 색칠하기
'''
10 x 10 격자
칠이 끝난 후 보라색이 되는 칸 수
T : 테스트 케이스
N : 칠할 영역의 개수
r1, c1, r2, c2, color
color 1 = red 2 = blue
'''

import sys
sys.stdin = open('input1.txt', 'r')
T = int(input())
for t in range(T):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                arr[i][j] += color
    purple = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                purple += 1
    print(f'#{t+1} {purple}')
