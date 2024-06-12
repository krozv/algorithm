'''
V E: V 1~V번까지의 V개의 정점. E개의 간선
E개의 간선정보
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(s, N):
    """
    param s: 시작정점
    param N: 노드 개수
    """
    # 큐
    q = []
    # visited
    visited = [0]*(N+1)
    # 시작점 인큐
    q.append(s)
    # 시작점 방문표시
    visited[s] = 1
    # 큐가 비워질때까지... (남은 정점이 있으면)
    while q:
        t = q.pop(0)
        # t에서 할 일
        print(t)
        for i in adjl[t]:   # t에 인접인 정점
            if not visited[i]:
                q.append(i)     # 인큐
                visited[i] = 1 + visited[t]  # 방문표시 -> 깊이를 알 수 있음
    print(visited)


V, E = map(int, input().split())
arr = list(map(int, input().split()))
# 인접리스트
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
bfs(4, V)