# 단순 2진 암호코드
"""
비율로 풀기 생각해보자 0과 1의 비율
"""

import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    password = []
    for i in range(N):
        for j in range(M-1, 0, -1):
            if 1 in arr[i]:
                if arr[i][j] == 1:
                    k = j
                    password = arr[i][k-55:k+1]
                    break
    # 1. dictionary로 풀기
    info = {'0001101': 0,
            '0011001': 1,
            '0010011': 2,
            '0111101': 3,
            '0100011': 4,
            '0110001': 5,
            '0101111': 6,
            '0111011': 7,
            '0110111': 8,
            '0001011': 9}
    code = []
    for i in range(0, 56, 7):
        p = list(map(str, password[i:i+7]))
        c = info[''.join(p)]
        code.append(c)
    output = 0
    s = 0
    for idx, val in enumerate(code):
        if idx % 2: # idx가 홀수
            output += val
        else:
            output += val * 3
        s += val
    if output%10:
        print(f'#{t} 0')
    else:
        print(f'#{t} {s}')

