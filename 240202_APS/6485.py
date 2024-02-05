# 6485. 삼성시의 버스 노선
'''
1. 입력받은 A~B쌍에 대해서 1씩 더한 count 행렬 만들기
    - count 행렬 0~5000 index 만들 수 있음
    - count = [0] * 5001
    for i : 0 -> N-1
        A, B = input()
        for j : A -> B
            counts[j] += 1
    p = input()
    for i : 0 -> P
        c = int(input()
        print(counts[c])

2.
'''
T = int(input())
for t in range(1, T+1):
    N = int(input())
    counts = [0] * 5001
    # N개의 노선을 정류장에 표시
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1): # 1<=A<=B<=5000
            counts[j] += 1
    P = int(input())
    busstop = [int(input()) for _ in range(P)]

    print(f'#{t}', end=' ')
    for i in busstop: # 출력할 버스 정류장의 번호
        print(counts[i], end=' ')
    print()
