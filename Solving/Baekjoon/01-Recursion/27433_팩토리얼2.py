# 팩토리얼 2
import sys
input = sys.stdin.readline


def f(i):
    global result
    if i == N+1:
        print(result)
        return
    result *= i
    f(i+1)


N = int(input())
result = 1
f(1)