# 15651
import sys
input = sys.stdin.readline

def f(i):
    if i == M:
        print(' '.join(map(str, path)))
        return
    for j in range(1, N+1):
        path.append(j)
        f(i+1)
        path.pop()


path = []
N, M = map(int, input().split())
f(0)