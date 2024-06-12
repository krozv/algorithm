import sys
sys.stdin = open('input.txt', 'r')
from heapq import heappush, heappop


def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0
    while pq:
        dist, now = heappop(pq)
        if distance[now] < dist:
            continue

        for next in adj[now]:
            next_dist = next[0]
            next_node = next[1]

            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue
            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))


T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    distance = [int(1e9)] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s].append([w, e])
    dijkstra(0)
    print(f'#{t} {distance[-1]}')

