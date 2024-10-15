# 12100. 2048(Easy)
"""
블록 추가 X
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없음
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록
4 * 4 * 4 * 4 * 4 = 16 * 16 * 4 = 16 * 64 = 1024번
시간 1초
1,000,000,000번
약 1번에 최대 1,000,000번
1 <= N <= 20
필요한 함수
1. 방향에 따라 블록 이동
2. 이동된 블록 합치기
3. 최대값 계산
방향은 direction list 만들어놓고, 조합  사용해서 만들까?
4. 백트래킹 ->
4-1. 이미 나올 수 있는 최댓값이 나온 경우 stop
4-2. 더 진행해도 최댓값 불가할 경우(2^x 다음과 2^y)일 경우
남은 턴 n 일때
2^x와 2^y가 합쳐지려면 필요한 턴 개수(x-y)이것보다 남은 턴이 적을때 그만
"""
import sys
from itertools import product

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find_max_value():
    return 10


def move_block(arr, dir):
    di, dj = dir
    return arr

def combine_block(arr):
    return arr


# input
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 만들 수 있는 최댓값 구하기
max_val = find_max_value()

# 가능한 방향의 조합 구하기(direction의 index)
cases = list(product(range(0, 4), repeat=5))
# 가능한 방향에 따라 최댓값 계산
for case in cases:
    # case = [0, 0, 0, 0, 0] 방향 리스트임
    
    for dir in case:
        # backtracking
        # 1. 이미 max_val 나온 경우
        # 2. 더 진행해도 최댓값 나오지 않을 경우

        # 방향에 따른 블록 이동
        arr = move_block(arr, direction[dir])
        # 이동된 블록 합치기
        arr = combine_block(arr)
        # 현재까지의 최댓값 current_max 계산

        pass