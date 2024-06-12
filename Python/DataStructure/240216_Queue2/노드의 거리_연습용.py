# 노드의 거리 외워서 짜기
"""
bfs(breadth first search)

"""
def bfs(start, end):
    """
    start: 출발 지점
    end: 도착 지점
    """
    v = [0] * (V+1)     # 방문한 곳 표시 예정
    q = []
    v[start] = 1
    q.append(start)
    while q:
        c = q.pop(0)    # 큐에서 pop한 현재 위치
        if c == end:
            return v[c] - 1
        for i in adj[c]:
            if not v[i]:
                q.append(i)
                v[i] = 1 + v[c]
    return 0



# 입력
import sys
sys.stdin = open("input1.txt", 'r')

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)
    S, G = map(int, input().split())
    print(f'#{t} {bfs(S, G)}')