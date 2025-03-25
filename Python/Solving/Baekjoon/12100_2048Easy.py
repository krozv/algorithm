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
from copy import deepcopy

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


# array안에서 만들 수 있는 최댓값 구하는 함수
# 그냥 최댓값 구하는 함수 아님
def find_max_value(arr):
    total = 0
    for row in arr:
        total += sum(row)
    cnt = 0
    while total > 1:
        total //= 2
        cnt += 1
    return 2**cnt


# 방향 delta에 따라서 블럭 이동하는 함수
def move_block(block, delta):
    arr = deepcopy(block)
    # 방향에 따라서 시작점 다름
    """
    상(-1, 0): 세로 방향으로 0부터
    하(1, 0): 세로 방향으로 N-1부터
    좌(0, -1): 가로 방향으로 0부터
    우(0, 1): 가로 방향으로 N-1부터
    """

    # 예시: 상(-1, 0)일 때
    if delta == (-1, 0):
        for j in range(N):
            for i in range(1, N):
                for k in range(1, i+1):
                    if arr[i-k][j] == 0:
                        arr[i-k][j], arr[i-k+1][j] = arr[i-k+1][j], arr[i-k][j]
    # 예시: 하(1, 0)일 때
    if delta == (1, 0):
        for j in range(N):
            for i in range(N-2, -1, -1):
                for k in range(1, N-i):
                    if arr[i+k][j] == 0:
                        arr[i+k][j], arr[i+k-1][j] = arr[i+k-1][j], arr[i+k][j]

    # 좌(0, -1)일 때
    if delta == (0, -1):
        for i in range(N):
            for j in range(1, N):
                for k in range(1, j+1):
                    if arr[i][j-k] == 0:
                        arr[i][j-k], arr[i][j-k+1] = arr[i][j-k+1], arr[i][j-k]

    # 우 (0, 1)일 때
    if delta == (0, 1):
        for i in range(N):
            for j in range(N-2, -1, -1):
                for k in range(1, N-j):
                    if arr[i][j+k] == 0:
                        arr[i][j+k], arr[i][j+k-1] = arr[i][j+k-1], arr[i][j+k]
    return arr


# 같은 블럭 결합하는 함수
def combine_block(block, delta):
    arr = deepcopy(block)
    # 예시: 상(-1, 0)일 때
    if delta == (-1, 0):
        for j in range(N):
            for i in range(1, N):
                if arr[i-1][j] == arr[i][j]:
                    arr[i-1][j] *= 2
                    arr[i][j] = 0
    # 예시: 하(1, 0)일 때
    if delta == (1, 0):
        for j in range(N):
            for i in range(N-2, -1, -1):
                if arr[i+1][j] == arr[i][j]:
                    arr[i+1][j] *= 2
                    arr[i][j] = 0
    # 좌(0, -1)일 때
    if delta == (0, -1):
        for i in range(N):
            for j in range(1, N):
                if arr[i][j-1] == arr[i][j]:
                    arr[i][j-1] *= 2
                    arr[i][j] = 0
    # 우 (0, 1)일 때
    if delta == (0, 1):
        for i in range(N):
            for j in range(N-2, -1, -1):
                if arr[i][j+1] == arr[i][j]:
                    arr[i][j+1] *= 2
                    arr[i][j] = 0
    return arr


# arr안의 가장 큰 값, 두번째로 큰 값 리턴하는 함수
def find_val(arr):
    total = []
    for row in arr:
        total.extend(row)
    total.sort(reverse=True)
    if len(total) > 1:
        return total[0], total[1]
    return total[0], None


# 지수 구하는 함수
def calculate_factor(num):
    if not num:
        return None
    cnt = 0
    while num != 1:
        num //= 2
        cnt += 1
    return cnt


def dfs(cnt, val1, val2, arr, delta):
    """
    cnt: 현재 이동횟수
    val1: 가장 큰 값
    val2: 두번째로 큰 값
    arr: 현재 블럭 배열
    """

    global max_val, result
    # backtracking
    # 1. 이미 max_val 나온 경우
    if val1 == max_val:
        return val1
    # 2. 더 진행해도 최댓값(result) 나오지 않을 경우
    a = calculate_factor(val1)
    b = calculate_factor(val2)
    if (a - b) > (5 - cnt):
        return val1
    # 3. cnt == 5: return val
    if cnt == 5:
        return val1

    block = deepcopy(arr)
    # 방향에 따른 블록 이동
    moved_block = move_block(block, delta)

    # 이동된 블록 합치기
    combined_block = combine_block(moved_block, delta)

    completed_block = move_block(combined_block, delta)
    # block 이동 안했을 경우 그냥 return
    if completed_block == arr:
        return val1
    # 현재까지의 최댓값 current_max 계산 val1, val2
    val1, val2 = find_val(completed_block)
    val = 0
    for d in direction:
        val = dfs(cnt+1, val1, val2, completed_block, d)
    return val

# input
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 만들 수 있는 최댓값 구하기
max_val = find_max_value(arr)
# 가능한 방향에 따라 최댓값 계산
result = 0
# val1, val2 탐색 후 dfs
val1, val2 = find_val(arr)

block = deepcopy(arr)
val = 0
for delta in direction:
    val = max(val, dfs(0, val1, val2, block, delta))
print(val)