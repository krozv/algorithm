# 노드의 합 (제출용)
"""
완전 이진 트리
리프 노드에 1000이하의 자연수가 저장
루트 = 1
"""
T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    h = [0] * (N+1)
    for _ in range(M):
        leap, num = map(int, input().split())
        h[leap] = num
    # h[L] = ?
    last = N
    while 1 < last:
        p = last // 2
        c = p * 2
        # h[c+1]이 존재할 경우
        if c+1 <= N:
            h[p] = h[c] + h[c+1]
        else:
            h[p] = h[c]
        last -= 2
    print(f'#{t} {h[L]}')