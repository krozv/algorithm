def dfs(i):
    # 인덱스에 해당하는 지점에 방문함을 표시
    visited[i] = 1
    # 방문한 정점을 프린트
    print(i)
    # 현재 위치한 정점에서 인접하고 방문 안 한 정점(visited == 0)이 있다면 방문
    for w in adj[i]:
        if visited[w] == 0:
            print(w)
            dfs(w)


V, E = map(int, input().split())
# V: 정점 개수
# E: edge 개수
arr = list(map(int, input().split()))

# 인접리스트
adj = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adj[n1].append(n2)
    adj[n2].append(n1)
# 방명록 만듦
visited = [0]*(V+1)
dfs(1)  # 1번 정점부터 경로 탐색 시작
