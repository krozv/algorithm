# 그래프 경로
"""
V개 이내의 노드를 E개의 간선으로 연결
특정한 두 개의 노드에 경로가 존재하는 지 확인하는 프로그램 만들기
경로 있으면 1, 없으면 0
노드는 1번부터 존재
V개의 노드 중 간선으로 연결되지 않는 경우도 존재
"""
def dfs(v):
    """
    param v: start node
    """
    # 방명록에 체크
    visited[v] = 1
    # 이동할 노드 탐색
    edge = False
    for w in adj[v]:
        if w == G:
            edge = True
            return edge
        if visited[w] == 0:
            visited[w] = 1
            if not edge:
                edge = dfs(w)
            else:
                return edge
    else:
        return edge

import sys
sys.stdin = open('sample_in (1).txt', 'r')
T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split()) # 5<=V<= 50, 4<=E<=1000
    arr = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for info in arr:
        [n1, n2] = info
        adj[n1].append(n2)

    visited = [0] * (V+1)
    print(f'#{t} {int(dfs(S))}')
