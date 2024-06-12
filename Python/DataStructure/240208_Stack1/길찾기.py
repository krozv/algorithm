# 길찾기
"""
A 도시에서 B 도시로 이동할 거
출발점 0, 도착점 99
정점의 개수는 98개
길의 개수 2개 안넘어감
"""
def dfs(v):
    # 방문 표시
    visited[v] = 1
    arrived = False
    # 다음 경로 이동
    for w in adj[v]:
        if w == 99:
            arrived = True
            return arrived
        if visited[w] == 0:
            visited[w] = 1
            if not arrived:
                arrived = dfs(w)
    else:
        return arrived

import sys
sys.stdin = open('input (13).txt', 'r')
while True:
    try:
        t, E = map(int, input().split())
        arr = list(map(int, input().split()))
        adj = [[] for _ in range(100)]
        for i in range(E):
            adj[arr[i*2]].append(arr[i*2+1])
        visited = [0] * 100
        print(f'#{t} {int(dfs(0))}')
    except EOFError:
        break
