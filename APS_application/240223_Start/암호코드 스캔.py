# 암호코드 스캔
"""

"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    # print(arr)
    password = [0] * N
    # 16진수를 2진수로 변경한다
    for i in range(N):
        for j in range(M):
            arr[i][j] = format(int(arr[i][j], 16), '04b')
        password[i] = ''.join(arr[i])
    print(password)
    start = end = 0
    for i in range(N):
        if '1' in password[i]:
            for j in range(N-1, N-56-1, -1):
                if password[i][j] == '1':
                    end = j
                    start = end - 56 + 1
                    print(password[i][start], password[i][end])
                    break




    # 검증코드를 확인하여 정상적인 암호코드인지 확인
    # 정상적인 암호코드 판별한 뒤 숫자들의 합 출력