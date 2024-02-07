# 숫자 배열 회전
"""
T 테스트 케이스
N x N 행렬 3<=N<=7
90도 180도 270도 회전한 거 출력
"""
def rotation_90(arr:[], N:int):
    deg_90 = [[0] for _ in range(N)]
    for i in range(N):
        deg_90[i] = ''
        for j in range(N):
            deg_90[i] = str(deg_90[i]) + str(arr[N-1-j][i])
    return deg_90

import sys
sys.stdin = open('input_rotation.txt','r')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_90 = rotation_90(arr, N)
    arr_180 = rotation_90(arr_90, N)
    arr_270 = rotation_90(arr_180, N)
    new_arr = [[0]*3 for _ in range(N)]
    for i in range(N):
        new_arr[i][0] = str(arr_90[i])
        new_arr[i][1] = str(arr_180[i])
        new_arr[i][2] = str(arr_270[i])
    print(f'#{t}')
    for i in range(N):
        print(*new_arr[i])