# 9019. DSLR
"""
레지스터 0<= n <10,000 십진수 저장가능

D
- n을 2배로 바꾼다
- 결과 값이 9999보다 클 때는 10000으로 나눈 나머지
S
- (n-1)
- n == 0 -> 9999
L
- 1234 -> 2341
R:
- 1234 -> 4123
# bfs + queue
"""
import sys
from collections import deque
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
input = sys.stdin.readline
debug = True

def debug_print(text):
    if debug: print(text)

def calculate(A, B):
    """
    A, B: string으로 이루어진 두 숫자
    return: 명령어
    """
    q = deque()
    visited = [0] * 10000
    q.append([A, ''])
    cnt = 0
    while q:
        if cnt > 3:
            break
        num, command = q.popleft()
        visited[int(num)] = 1
        # debug_print(num)
        debug_print(num)
        debug_print(command)
        # B랑 비교
        if A == B:
            break
        # D
        d_num = 0
        if int(num) * 2 >= 9999:
            d_num = int(num) * 2 % 10000 
        else:
            d_num = int(num) * 2
        if not visited[d_num]:
            q.append([str(d_num), command+'D'])
        # S
        s_num = 0
        if int(num) == 0:
            s_num = 9999
        else:
            s_num = int(num) - 1
        if not visited[s_num]:
            q.append([str(s_num), command+'S'])
        # L
        l_num = num[1:] + num[0]
        if not visited[int(l_num)]:
            q.append([l_num, command+'L'])
        # R
        r_num = num[-1] + num[:-1]
        if not visited[int(r_num)]:
            q.append([r_num, command+'R'])
        # cnt += 1
    return command

def solution():
    T = int(input())
    for _ in range(T):
        A, B = input().split()
        num_A, num_B = A.zfill(4), B.zfill(4)
        res = calculate(num_A, num_B)
        print(res)

if __name__ == "__main__":
    solution()