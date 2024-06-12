import sys
sys.stdin = open('input.txt', 'r')

def dij(s, N, adj, D):
    """
    s: 출발점
    N: 마지막노드
    adj: 참고할 인접 행렬
    D: 최소비용 테이블
    """
    # U = {s} 비용 결정된 노드의 집합
    U = [0]*(N+1)
    U[s] = 1
    # 출발점을 제외한 나머지 정점만큼 반복, while U!=V
    for _ in range(N-1):
        # V-U 원소 중에서 D[w]가 최소인 정점 w 선택
        min_w = INF
        w = 0
        for i in range(1, N+1):
            if U[i] == 0 and min_w > D[i]:
                min_w = D[i]
                w = i
        # V-U 원소 중에서 D[w]가 최소인 정점 w를 U에 포함
        U[w] = 1
        # w에 인접한 정점에 대해, 기존 비용과 w를 거쳐가는 비용을 비교
        for i in range(1, N+1):
            if 0<adj[w][i]<INF:
                D[i] = min(D[i], D[w]+adj[w][i])


T = int(input())
for t in range(1, T+1):
    N, M, X = map(int, input().split())

    INF = 1e9

    # 인접행렬: 인수의 집에서 귀가하는 최단 거리 구하기용
    # adj1[i][j]: i에서 j로 가는데 걸리는 시간
    adj1 = [[INF]*(N+1) for _ in range(N+1)]
    adj2 = [[INF]*(N+1) for _ in range(N+1)]

    for i in range(N+1):
        adj1[i][i] = 0

    for _ in range(M):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[y][x] = c

    D1 = [0]*(N+1)  # X에서 각자의 집으로 귀가하는 시간
    for i in range(1, N+1):
        D1[i] = adj1[X][i]  # 초기 그래프에서 X에서 각 정점까지의 거리(비용)

    dij(X, N, adj1, D1)

    D2 = [0] * (N + 1)  # X에서 각자의 집으로 귀가하는 시간
    for i in range(1, N + 1):
        D2[i] = adj2[X][i]  # 초기 그래프에서 X에서 각 정점까지의 거리(비용)

    dij(X, N, adj2, D2)

    ans = [0]*(N+1)
    for i in range(N+1):
        ans[i] = D1[i] + D2[i]
    print(f'#{t} {max(ans)}')


