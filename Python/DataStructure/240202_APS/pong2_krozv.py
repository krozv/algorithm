# 풍선팡 2
"""
T 테스트 케이스
N x M 격자판
Array 꽃가루 개수 들어있음
꽃가루 수 중 최댓값을 출력
"""
import sys
sys.stdin = open('input_pang2_add_case.txt', 'r')
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0 # 최대 꽃가루 개수
    for i in range(N):
        for j in range(M):
            cnt = arr[i][j]     # 꽃가루 개수 셀 거임
            for k in range(4):  # delta 이용해서 주변 값 합칠 거임
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<M:
                    cnt += arr[ni][nj]
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{t} {max_cnt}')
