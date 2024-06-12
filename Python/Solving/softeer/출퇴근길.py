import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def bfs(start, end, visited):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        if now == end:
            continue
        if now != start:
            visited[now] = now
        for to in adj[now]:
            if not visited[to]:
                q.append(to)


from collections import deque
n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
start, end = map(int, input().split())

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)
bfs(start, end, visited1)
bfs(end, start, visited2)
print(set(visited1))
print(set(visited2))
print(len(set(visited1)&set(visited2))-1)


