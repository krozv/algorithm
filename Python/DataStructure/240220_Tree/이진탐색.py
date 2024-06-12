# 이진탐색
"""
완전 이진 트리가 되도록 만들면 효율적
루트에 저장된 값과 N//2번 노드에 저장된 값 출력
"""
def in_order(T):
    if T:
        if left[T] and visited[left[T]]==0:
            in_order(left[T])
        else:
            visited[T] = 1
            node[T] = val.pop(0)
            if right[T] and visited[right[T]] == 0:
                in_order(right[T])
            if par[T] and visited[par[T]] == 0:
                in_order(par[T])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    # node 만들기 - 완전 이진 트리로 만들기
    par = [0] * (N+1)
    left = [0] * (N+1)
    right = [0] * (N+1)
    for i in range(1, N+1):
        # 1 ~ N까지 출력됨 -> 이진 트리 만들예정
        if i*2 < N+1:
            left[i] = i * 2
            par[i * 2] = i
        if i*2+1 < N+1:
            par[i*2+1] = i
            right[i] = i * 2 + 1
    # node에 값 넣기 - 중위순회로 넣기
    # 가장 아래 + 왼쪽인 수 찾기
    l = 1
    while left[l]:
        l = left[l]
    visited = [0] * (N+1)
    val = list(range(1, N+1))
    node = [0] * (N+1)
    in_order(l)
    print(f'#{t} {node[1]} {node[N//2]}')