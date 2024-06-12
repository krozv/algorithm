'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i):
    """
    param i(v): 시작
    param V(N): 마지막
    """
    visited[i] = 1   # 시작점 방문
    print(i)        # 정점에서 할 일
    # 현재 방문한 정점에 인접하고 방문 안 한 정점이 있으면
    for w in adjl[i]:
        if visited[w] == 0:
            dfs(w)


V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트
adjl = [[] for _ in range(V+1)]     # adjl[i] 행에 i에 인접인 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)             # 방향이 없는 경우
visited = [0]*(V+1)
dfs(1)