# 파이프 옮기기 1
"""
(r, c)로 나타남
번호 1부터 시작함
파이프 회전 가능
N 3<=N<=16
파이프를 (1, 1) -> (N, N)으로 이동시키는 방법의 개수 구하기
하지만 나는 계산하기 귀찮아서 (0, 0) -> (N-1, N-1)로 풀 것임
delta = [[0, 1], [1, 0], [1, 1]
"""
import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

