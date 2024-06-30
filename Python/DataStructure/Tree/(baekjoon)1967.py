# 1967. 트리의 지름
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find_set(x):
    if x == parents[x]:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

n = int(input())
edges = []
for _ in range(n-1):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])

# 가중치 기준으로 정렬
edges.sort(key=lambda x: x[2])
# parents 정보 저장
parents = [i for i in range(n+1)]

sum_weight = 0
cnt = 0

# 가중치 계산
for s, e, w in edges:
    print(s, e, w)
    if find_set(s) == find_set(e):
        continue
    cnt += 1
    union(s, e)
    sum_weight += w
    if cnt == n-1:
        break

print(sum_weight)