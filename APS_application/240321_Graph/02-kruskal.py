# 1. 전체 그래프를 보고, 가중치가 제일 작은 간선부터 뽑음
# -> 코드로 구현: 전체 간선 정보를 저장 + 가중치로 정렬
# 2. 방문 처리
# -> 이때, 싸이클이 발생하면 안된다!
# -> 싸이클 여부? -> union-find algorithm 활용

import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    if x == parents[x]:
        return x
    # 경로 압축
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    # 이미 같은 집합에 속해있다면 continue
    if x == y:
        return
    # 다른 집합이라면 합침
    # 예: 더 작은 루트 노드에 합쳐라
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


V, E = map(int, input().split())
# 간선 정보 저장
edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append([s, e, w])
# 가중치 w 기준으로 정렬
edges.sort(key=lambda x: x[2])
# 대표자 찾기 위한 배열
parents = [i for i in range(V)]

sum_weight = 0
cnt = 0
# 간선들을 모두 확인
for s, e, w in edges:
    print(s, e, w)
    # 싸이클이 발생하면 pass
    # -> 이미 같은 집합에 속해 있다면 pass = 싸이클 발생하므로
    if find_set(s) == find_set(e):
        continue
    cnt += 1
    # 싸이클이 없으면 방문 처리
    union(s, e)
    sum_weight += w
    # 노드를 모두 다 들리면 break
    if cnt == V - 1:
        break

print(f'최소비용 {sum_weight}')
