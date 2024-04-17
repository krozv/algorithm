# 최고의 집합
def solution(n, s):
    from itertools import product
    comb = list(product(range(1, s), repeat=n))
    temp = []
    for c in comb:
        if sum(c) == s:
            mul = 1
            for num in c:
                mul *= num
            temp.append([list(c), mul])

    if len(temp) == 0:
        answer = [-1]
    # 곱이 최대인 집합 구하기
    else:
        temp.sort(key=lambda x: -x[1])
        answer = temp[0][0]
    return answer

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = 3
for t in range(3):
    n, s = map(int, input().split())
    print(solution(n, s))