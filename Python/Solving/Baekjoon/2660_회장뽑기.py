# 2660. 회장뽑기
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
adj = [[] * (N+1) for _ in range(N+1)]
arr = [[0] * (N+1) for _ in range(N+1)]

def check(start, curr, cnt):
    for node in adj[curr]:
        if (cnt+1 < arr[start][node] or not arr[start][node]) and start != node:
            arr[start][node] = cnt+1
            check(start, node, cnt+1)

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, N+1):
    check(i, i, 0)

min_score = 1e9
result = []
for i in range(1, N+1):
    if min_score > max(arr[i]):
        min_score = min(min_score, max(arr[i]))
        result = []

    if min_score == max(arr[i]):
        result.append(i)

print(min_score, len(result))
print(' '.join(map(str, result)))