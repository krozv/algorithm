# 풍선팡
'''
T 테스트 케이스
N x M 가로 세로
arr 풍선 안에 든 꽃가루 개수
가운데 풍선 터뜨리면 상하좌우 풍선 팡
'''
import sys
sys.stdin = open('input_pang.txt', 'r')
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # 3 <= N, M <= 100
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0 # 최대 꽃가루임
    for i in range(N):
        for j in range(M):
            add = arr[i][j] # 추가로 터지는 풍선 개수
            cnt = arr[i][j] # 꽃가루 담을 그릇
            for k in range(4):
                for m in range(add):
                    ni = i + di[k] * (m+1)
                    nj = j + dj[k] * (m+1)
                    if 0<=ni<N and 0<=nj<M:
                        cnt += arr[ni][nj]
            if max_cnt < cnt:
                max_cnt = cnt
    print(f'#{t} {max_cnt}')
