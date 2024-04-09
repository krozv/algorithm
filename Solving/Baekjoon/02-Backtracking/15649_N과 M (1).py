# 15649
import sys
input = sys.stdin.readline
def f(s):
    """
    s: 선택한 숫자의 개수
    """
    # 기저
    if s == M:
        print(' '.join(map(str, path)))
        return

    # 수열 쌓기
    for i in range(1, N+1):
        if i not in path:
            path.append(i)
            f(s+1)
            path.pop()


N, M = map(int, input().split())
path = []
f(0)
