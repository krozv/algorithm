# 암호코드 스캔
"""

"""
def find_code(l):
    code = ''   # 찾은 암호 (string)
    c = 56 * l  # 암호의 길이
    code_lst = []
    while True:
        for i in range(N):
            j = N-1
            while j > N-c-1:
                # print(code_lst)
                if password[i][j] == '1':
                    end = j
                    start = j - c + 1
                    j = start - 1
                    if password[i][start:end+1] not in code_lst:
                        code_lst.append(password[i][start:end+1])
                else:
                    j -= 1
        print(code_lst)
        break


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())    # N * M 행렬
    arr = [list(input()) for _ in range(N)]
    password = [0] * N
    # 16진수를 2진수로 변경
    for i in range(N):
        for j in range(M):
            arr[i][j] = format(int(arr[i][j], 16), '04b')
        password[i] = ''.join(arr[i])
        # if '1' in password[i]:
            # print(password[i]) # 암호코드 한줄이 str로 이루어져있는 리스트
    test = 1
    i = 1
    while test < N:
        find_code(test)
        i += 1
        test *= i
    # 검증코드를 확인하여 정상적인 암호코드인지 확인
    # 정상적인 암호코드 판별한 뒤 숫자들의 합 출력