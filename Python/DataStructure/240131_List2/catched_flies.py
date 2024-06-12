# 파리 퇴치~~~
'''
N x N 배열
M x M으로 파리 잡을 것
5 <= N <= 15
2 <= M <= N
파리 개수 최대 30마리 으으으
'''
import sys
sys.stdin = open('input2.txt', 'r')
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 파리채를 만듦
    di = [[0]*M for _ in range(M)]
    dj = [[0]*M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            di[i][j] = i
            dj[i][j] = j
    # print(di, dj)
    catched_files = [[0]*(N-M+1) for _ in range(N-M+1)]
    # 파리 잡으러 가자
    max_catched_files = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for r in range(M):
                for c in range(M):
                    p = i + di[r][c]
                    q = j + dj[r][c]
                    catched_files[i][j] += arr[p][q]
            if max_catched_files < catched_files[i][j]:
                max_catched_files = catched_files[i][j]
    # 제일 많이 잡은 파리수는?
    print(f'#{t+1} {max_catched_files}')

