import sys
input = sys.stdin.readline

def f(i):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    for j in range(i, N+1):
        if j not in path:
            path.append(j)
            f(j)
            path.pop()


path = []
N, M = map(int, input().split())
f(1)