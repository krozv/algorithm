"""
N = X^3이 되는 양의 정수 N
"""
def get_result(n):
    i = 2
    cnt = {}

    while True:
        if n == 1:
            break
        if n % i == 0:
            n //= i
            if cnt.get(i):
                cnt[i] += 1
            else:
                cnt[i] = 1
        else:
            i += 1
            if cnt.get(i-1) and cnt[i-1] % 3 != 0:
                return -1

    result = 1
    for key, val in cnt.items():
        if not val % 3:
            result *= key ** (val//3)
        else:
            return -1
    return result


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    print(f'#{t} {get_result(N)}')