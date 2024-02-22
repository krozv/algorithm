# 중위순회
"""
중위순회를 사용하여 특정 단어 찾기
"""
######################수정해야함#########################
def in_order(T):
    if T:
        # print(T)
        # print(visited)
        if left[T] and visited[left[T]]==0:
            in_order(left[T])
        else:
            visited[T] = 1
            global string
            string += arr[T-1][1]
            if right[T] and visited[right[T]]==0:
                in_order(right[T])
            if par[T] and visited[par[T]]==0:
                in_order(par[T])



for t in range(1, 11):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    # print(arr)
    # 해당 정점, 정점 문자, 왼쪽 자식, 오른쪽 자식
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)
    visited = [0] * (N + 1)
    for i in range(N):
        n, c, *child = arr[i]
        l = r = 0
        n = int(n)
        if child:
            l, *r = child
            l = int(l)
            par[l] = n
            if r:
                r = int(r[0])
                par[r] = n
            else:
                r = 0
        left[n] = l
        right[n] = r
    # print(par)
    # print(left)
    # print(right)
    string = ''
    c = 1
    while left[c] != 0:
        c = left[c]
    in_order(c)
    print(f'#{t} {string}')

