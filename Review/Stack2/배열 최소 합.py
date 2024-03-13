# 배열 최소 합
def f(i, n, s):
    """
    i: 현재 인덱스 위치
    n: 선택해야 할 원소 개수
    s: 선택한 원소의 합
    """
    



T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    f(0, N, 0)