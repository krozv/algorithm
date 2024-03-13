# 그래프 경로
"""
경로가 있으면 1
없으면 0 출력
"""

"""
dfs 함수 짜야함
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
    S, G = map(int, input().split())
    v = [0] * (V+1)
    stk = [S]
    print(f'#{t} {int(dfs(S))}')