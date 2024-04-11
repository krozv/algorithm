# 피보나치수 5
import sys
input = sys.stdin.readline


def f(i, s1, s2):
    if i == n:
        print(s1)
        return
    s1, s2 = s2, s1+s2
    f(i+1, s1, s2)


n = int(input())
f(0, 0, 1)
