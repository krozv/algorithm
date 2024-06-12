# 인접 리스트
    # V개의 노드가 갈 수 있는 정보만 저장
# 장점
    # 메모리 사용량이 적음
    # 탐색할 때 갈 수 있는 곳만 확인하기 때문에 시간적으로 효율
# 단점
    # 노드 간 연결 정보를 확인하기 어려움
    # 특정 노드 간 연결 여부를 확인하는 데 시간이 걸림
graph = [
    [1, 3],
    [0, 2, 4],
    [1],
    [0, 4],
    [1, 3],
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
        for to in graph[now]:
            if visited[to]:
                continue

            visited[to] = 1
            queue.append(to)


bfs(0)