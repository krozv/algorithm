# 5250. 최소 비용
"""
최적경로 이동, 최소한의 연료로 이동
출발: 맨 왼쪽 위
도착: 맨 오른쪽 아래
높이가 높은 곳으로 이동 시 -> 높이 차이만큼 연료 소비
prim algorithm으로 해보기
"""
import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop
def dijkstra(start):
    pq = []
    x, y = start
    # 시작점의 weight, node 번호를 한 번에 저장
    heappush(pq, (0, start))
    # 시작 노드 초기화
    distance[x][y] = 0
    while pq:
        delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        # 최단 거리 노드에 대한 정보
        dist, now = heappop(pq)

        # now가 이미 더 짧은 거리로 온 적이 있다면 pass
        if distance[now[0]][now[1]] < dist:
            continue

        # now에서 인접한 다른 노드 확인
        for d, w in enumerate(graph[now[0]][now[1]]):
            if not w:
                continue
            next_dist = w
            next_i = now[0]+delta[d][0]
            next_j = now[1]+delta[d][1]
            # next_node = [now[0]+delta[d][0], now[1]+delta[d][1]]

            # 누적 거리 계산
            new_dist = dist + next_dist

            # 이미 더 짧은 거리로 간 경우 pass
            if new_dist >= distance[next_i][next_j]:
                continue

            # 누적 거리를 최단 거리로 갱신
            distance[next_i][next_j] = new_dist
            # next_node의 인접 노드들을 pq에 추가
            heappush(pq, (new_dist, [next_i, next_j]))

INF = int(1e9)
T = int(input())
for t in range(1, T+1):
    N = int(input())  # 3<=N<=100
    arr = [list(map(int, input().split())) for _ in range(N)]  # 0<=H<1000

    # 인접 행렬
    graph = [[[0]*4 for _ in range(N)] for _ in range(N)]
    # 정보 저장
    for i in range(N):
        for j in range(N):
            delta = [[0, 1], [1, 0]]
            for k in range(2):
                ni = i + delta[k][0]
                nj = j + delta[k][1]
                if 0<=ni<N and 0<=nj<N:
                    if arr[ni][nj] > arr[i][j]:
                        graph[i][j][k+1] = arr[ni][nj] - arr[i][j] + 1
                        graph[ni][nj][(k+3)%4] = 1
                    else:
                        graph[i][j][k+1] = 1
                        graph[ni][nj][(k+3)%4] = arr[i][j] - arr[ni][nj] + 1


    # 누적 거리를 저장할 변수
    distance = [[INF]*N for _ in range(N)]
    dijkstra([0, 0])
    print(f'#{t} {distance[N-1][N-1]}')