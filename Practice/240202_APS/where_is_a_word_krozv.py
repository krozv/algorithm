# 어디에 단어가 들어갈 수 있을까?
'''
N x N 단어 퍼즐 5 <= N <= 15
K 특정 길이 2 <= K <= N
흰색 1 검은색 0
'''
import sys
sys.stdin = open('input_word.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    word = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 0 and j != N-1:
                if cnt == K:
                    word += 1
                cnt = 0
            else:
                if arr[i][j] == 1:
                    cnt += 1
                if j == N-1:
                    if cnt == K:
                        word += 1
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 0 and i != N-1:
                if cnt == K:
                    word += 1
                cnt = 0
            else:
                if arr[i][j] == 1:
                    cnt += 1
                if i == N-1:
                    if cnt == K:
                        word += 1

    print(f'#{t} {word}')

