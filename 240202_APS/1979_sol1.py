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

# T = int(input())
N = 6
K = 3
arr = [0, 1, 0, 1, 1, 1]

ans = 0
cnt = 0
for i in range(N):
    if arr[i]==0: # arr[i] == 0 일때 확인
        if cnt == K:
            ans += 1
        cnt = 0
    else:   # arr[i] == 1
        cnt += 1
        if i==N-1 and cnt==K: # 마지막 인덱스에 도착했을 때
            ans += 1
print(ans)
