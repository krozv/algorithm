# 영역나누기
"""
N x N 2차원 배열   2<=N<=20
1 <= 자연수 <= 100
배열의 행과 행, 열과 열 사이에 직선 (사분면)
각 영역 합의 최대값과 최소값의 차이가 가장 작은 경우
"""
import sys
sys.stdin = open('sample_in.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 오른쪽 아래 인덱스 정하기
    print(arr)