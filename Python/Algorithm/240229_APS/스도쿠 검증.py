# 스도쿠 검증
"""

"""
def row(n):
    num = list(range(1, 10))
    for j in range(9):
        if arr[n][j] in num:
            num.remove(arr[n][j])
        else:
            return False
    return True


def col(n):
    num = list(range(1, 10))
    for j in range(9):
        if arr[j][n] in num:
            num.remove(arr[j][n])
        else:
            return False
    return True


def square(n):
    num = list(range(1, 10))
    for i in range(3):
        for j in range(3):
            if arr[(n//3)*3+i][(n%3)*3+j] in num:
                num.remove(arr[(n//3)*3+i][(n%3)*3+j])
            else:
                return False
    return True


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    test = True
    for i in range(9):
        if test:
            test = row(i)
        if test:
            test = col(i)
        if test:
            test = square(i)
    print(f'#{t} {int(test)}')