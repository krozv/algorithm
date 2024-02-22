# 파리퇴치
'''
N x N 배열안에 파리 있음 5<=N<=15
M X M 크기의 파리채 2<=M<=N
죽은 파리의 개수를 구하라
'''
import sys
sys.stdin = open('input_flies.txt', 'r')

di = [0, 1]
dj = [1, 0]
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_flies = 0   # 가장 많이 잡은 파리 넣을 것
    for i in range(N):
        for j in range(N):
            flies = 0
            for k in range(M):
                ni = i + k
                for l in range(M):
                    nj = j + l
                    if 0<=ni<N and 0<=nj<N:
                        flies += arr[ni][nj]
            if max_flies < flies:
                max_flies = flies
    print(f'#{t} {max_flies}')