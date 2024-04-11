# 1697. 숨바꼭질
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    v = [0] * 100001
    v[start] = 1
    while q:
        now = q.popleft()
        if now == b:
            return v[now]-1
        for i in [now+1, now-1, now*2]:
            if 0<=i<100001 and not v[i]:
                v[i] = v[now] + 1
                q.append(i)


a, b = map(int, input().split())
arr = [range(0, 100001)]
print(bfs(a))