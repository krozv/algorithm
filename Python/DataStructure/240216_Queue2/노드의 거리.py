# 노드의 거리
'''
V E: V 1~V번까지의 V개의 정점. E개의 간선
E개의 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, N, G):
    """
    param s: 시작정점
    param N: 노드 개수
    """
    # 큐 생성
    q = []
    # visited 생성
    visited = [0] * (N+1)
    # 시작점 인큐
    q.append(s)
    # 인큐 표시
    visited[s] = 1
    # 처리안된 정점이 남아있으면
    while q:
        # 디큐
        t = q.pop(0)
        if t == G:
            return visited[t] - 1   # 최단 경로 간선 수
        # t에서 할 일
        print(t)
        for i in adjl[t]:   # t에 인접인 정점
            if not visited[i]:
                q.append(i)     # 인큐
                visited[i] = 1 + visited[t]  # 방문표시 -> 깊이를 알 수 있음
    print(visited)


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    # 인접리스트
    adjl = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjl[n1].append(n2)
        adjl[n2].append(n1)
    S, G = map(int, input().split())
    print(f'#{t} {bfs(S, V, G)}')