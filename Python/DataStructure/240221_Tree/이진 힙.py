# 이진 힙(제출용)
"""
이진 최소힙
완전 이진 트리 유지: 마지막 노드 뒤에 새 노드 추가
부모 노드 < 자식 노드 유지
새로 추가된 노드의 값이 조건에 맞지 않을 경우, 조건 만족할 때 까지 반복문 사용
마지막 노드의 조상 노드에 저장된 정수의 모두 합 출력
"""
def enq(N):
    global last
    last += 1
    h[last] = N
    c = last
    p = c // 2

    while p >= 1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c // 2


T = int(input())
for t in range(1, T+1):
    N = int(input())        # 노드의 수
    arr = list(map(int, input().split()))
    h = [0] * (N+1)
    last = 0
    for num in arr:
        enq(num)
    s = 0
    while h[last]:
        last = last // 2
        s += h[last]
    print(f'#{t} {s}')