"""
kruskal로 풀기
"""
import sys
sys.stdin = open('input.txt', 'r')

def find_set(x):
    # x의 부모가 자기 자신인지 확인
    if parents[x] == x:
        return x
    # 부모 찾기
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    # 이미 같은 집합이라면 return
    if x == y:
        return
    # 작은 거 기준으로 합칠 예정
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append([n1, n2, w])

    # 간선을 가중치 기준으로 정렬함
    edges.sort(key=lambda x: x[2])

    # 대표자 배열 생성
    parents = [i for i in range(V+1)]

    sum_weight = 0
    cnt = 1
    # 간선들을 모두 확인
    for s, e, w in edges:
        # 싸이클이 발생하면 pass
        if find_set(s) == find_set(e):
            continue
        # 싸이클이 아니라면, 부모 합쳐줌
        union(s, e)
        sum_weight += w
        cnt += 1
        # 노드를 모두 확인했다면,
        if cnt == V+1:
            break
    print(f'#{t} {sum_weight}')