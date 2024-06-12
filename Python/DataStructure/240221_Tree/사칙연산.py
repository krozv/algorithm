# 사칙연산
"""
사칙연산을 in-order로 이진 트리에 표현되어있음
이진트리의 계산 결과를 출력하라
그냥 이진트리임. 완전이진트리 아님
"""
for t in range(1, 11):
    N = int(input())
    h = [0] * (N+1)
    child = [0] * (N+1)
    op = ['+', '-', '*', '/']
    # 이진트리 입력 받음
    for _ in range(N):
        n, *info = input().split()
        n = int(n)
        # 연산자 정보가 포함된 경우
        if info[0] in op:
            h[n] = info[0]
            child[int(info[1])] = n
            child[int(info[2])] = n
        # 연산자 정보가 포함되지 않은 경우
        else:
            h[n] = int(info[0])
    last = N
    while 0 < last:
        p = child[last]
        c = p // 2
        if h[p] == '+':
            h[p] = h[last-1] + h[last]
        elif h[p] == '-':
            h[p] = h[last-1] - h[last]
        elif h[p] == '*':
            h[p] = h[last-1] * h[last]
        elif h[p] == '/':
            h[p] = float(h[last-1] / h[last])
        last -= 2
    print(f'#{t} {int(h[1])}')