# Prim 알고리즘
"""
heappush, heappop 공부하기. 무슨 의미인지?
continue와 pass의 차이 다시 익히기
"""
import sys
sys.stdin = open('input.txt', 'r')

from heapq import heappush, heappop

# bfs와 다른 점: 우선순위 큐 활용
def prim(start):
    pq = []
    # 최소비용신장트리: visited처럼 활용할 예정
    MST = [0] * V
    # 최소 비용
    sum_weight = 0
    # 시작점 추가
    # 기존 BFS: 노드 번호만 관리
    # PRIM: 가중치가 낮으면 먼저 나와야 함
    # -> 관리해야 할 데이터: 가중치, 노드 번호
    #       동시에 2가지 데이터 다루는 방법
    #       1. class 만들기: 한번에 3~4가지 데이터 활용할 경우는 class 활용하기
    #       2. tuple로 관리: 2가지 데이터는 활용 해도 괜찮음
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)
        print(now, MST)
        # 방문했다면 continue
        # PRIM: 일단 pq에 넣고 방문은 X
        # BFS: 무조건 방문
        if MST[now]:
            continue
        # 방문 처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight
        # 갈 수 있는 노드들을 보면서
        for to in range(V):
            # 갈 수 없다면 or 이미 방문했다면: pass
            if not graph[now][to] or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))

    print(f'최소비용 {sum_weight}')


V, E = map(int, input().split())
# 인접 행렬로 저장
# - [과제] 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s, e, w = map(int, input().split())
    # [가중치 그래프] 3 -> 4 로 가는데 31이라는 비용
    # graph[3][4] = 31
    graph[s][e] = w
    # 무방향 그래프: 반대방향도
    graph[e][s] = w
# print(graph)
prim(0)