# 인접 행렬 BFS
# 갈 수 있는 곳 다 가기
# 방문순서대로 다음 노드가 지정
# 먼저 방문 -> 먼저 다음 노드 FIFO
graph = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
]


def bfs(start):
    visited = [0] * 5

    # 시작 노드를 큐에 추가 + 방문 표시
    queue = [start]
    visited[start] = 1

    while queue:
        now = queue.pop(0)
        print(now, end=' ')

        # 갈 수 있는 곳을 체크
        for to in range(5):
            if graph[now][to] == 0:
                continue

            if visited[to]:
                continue

            visited[to] = 1
            queue.append(to)


bfs(0)