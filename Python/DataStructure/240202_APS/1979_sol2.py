# 1979. 어디에 단어가 들어갈 수 있을까
"""
N * N 크기의 단어 퍼즐을 만들 것
N=5, K=3이면 N * N 단어 퍼즐에서 길이가 3인 단어가 들어갈 수 있는 자리 찾기
5 <= N <= 15
2 <= K <= N
T
N, K
puzzle N*N 배열
흰색1, 검은색0
가로 또는 세로로 연속한 1의 개수가 K인 경우를 찾는 문제

Sol1.
1이면 count를 1씩 증가
0을 만나거나 마지막을 만났을 경우 초기화 -> 처리하기 귀찮으면 배열 마지막에 그냥 0추가해
"""
import sys
sys.stdin = open('input_1979.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    # 마지막 처리하기 귀찮으니까 0을 추가함
    arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
    N += 1  # 0인 열과 행 추가
    # 가로, 세로로 연속한 1의 개수가 K인 경우를 찾는 문제
    ans = 0
    for i in range(N): # 가로로 찾기
        cnt = 0     # i행에서 연속한 1의 개수를 찾음
        for j in range(N):
            if arr[i][j]:
                cnt += 1
            else:   # arr[i][j] == 0
                if cnt == K:
                    ans += 1
                cnt = 0
    for j in range(N): # 세로로 찾기
        cnt = 0     # i행에서 연속한 1의 개수를 찾음
        for i in range(N):
            if arr[i][j]:
                cnt += 1
            else:
                if cnt == K:
                    ans += 1
                cnt = 0
    print(f'#{t} {ans}')
