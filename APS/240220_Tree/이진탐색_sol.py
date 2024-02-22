# 현복 코드 보고 외우기
def inorder(T, end):
    global cnt, node
    if T > end:
        return 0
    if T:
        inorder(T * 2, end)
        node[T] = cnt
        cnt += 1
        inorder(T * 2 + 1, end)


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    node = [0] * (N + 1)
    cnt = 1
    inorder(1, N)
    print(f'#{tc} {node[1]} {node[N // 2]}')