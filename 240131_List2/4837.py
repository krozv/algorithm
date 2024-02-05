# 4837. 부분집합의 합
'''
부분집합 중
N개의 원소 & 원소의 합이 K인 부분집합의 개수
'''
A = list(range(1, 13))

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    count = 0
    # 부분 집합을 만듦
    for i in range(1 << 12):
        subset = set()
        set_len = 0
        for j in range(12):
            if i & (1 << j):
                subset.add(A[j])
                set_len += 1
        # 원소 N개이고, 합이 K인거 카운트
        if set_len == N:
            set_sum = 0
            for k in range(set_len):
                set_sum += k
            if sum(subset) == K:
                count += 1
    print(f'{t+1} {count}')