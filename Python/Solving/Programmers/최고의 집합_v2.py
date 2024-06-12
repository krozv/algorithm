def solution(n, s):
    if n > s:
        answer = [-1]
    else:
        answer = [int(s/n)] * n
        num = s - n * (int(s/n))
        a = -1
        for i in range(num):
            answer[a] += 1
            a -= 1
    return answer

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = 3
for t in range(3):
    n, s = map(int, input().split())
    print(solution(n, s))