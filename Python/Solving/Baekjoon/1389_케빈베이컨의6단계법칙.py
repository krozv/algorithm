# 1389
# 케빈 베이컨의 수가 가장 작은 사람
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
arr = [[0] * (N+1) for _ in range(N+1)]

def check(adj, start, curr, cnt):
    for node in adj[curr]:
        if (not arr[start][node] or arr[start][node] > cnt+1) and start != node:
            arr[start][node] = cnt+1
            check(adj, start, node, cnt+1)

for _ in range(M):
    a, b = map(int, input().split())
    if not adj[a].count(b):
        adj[a].append(b)
    if not adj[b].count(a):
        adj[b].append(a)

for i in range(1, N+1):
    check(adj, i, i, 0)

result = 0
number = 1e9
for i in range(1, N+1):
    if number > sum(arr[i]):
        number = sum(arr[i])
        result = i
print(result)