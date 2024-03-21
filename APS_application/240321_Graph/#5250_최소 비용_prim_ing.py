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


def prim(start):
    pq = []
    MST = [[0]*N for _ in range(N)]
    heappush(pq, (0, start))
    distance[start[0]][start[1]] = 0
    while pq:
        weight, now = heappop(pq)
        # 방문 처리
        MST[now[0]][now[1]] = 1
        # if weight >= sum:
        #     continue
        for d in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
            ni = now[0] + d[0]
            nj = now[1] + d[1]
            if 0<=ni<N and 0<=nj<N and MST[ni][nj]==0:
                a = 0
                if arr[ni][nj] > arr[now[0]][now[1]]:
                    a = arr[ni][nj] - arr[now[0]][now[1]]
                if [ni, nj] == [N-1, N-1]:
                    return
                heappush(pq, (1+a, [ni, nj]))
    return

T = int(input())
for t in range(1, T+1):
    N = int(input())  # 3<=N<=100
    arr = [list(map(int, input().split())) for _ in range(N)]  # 0<=H<1000
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    print(f'#{t} {prim([0, 0])}')
