# 15683. 감시
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# CCTV 감시 칸 체크 및 사각지대 개수 count
def find_black(i, cnt):
    """
    i: 체크하는 CCTV 번호
    cnt: 감시된 칸 수 count
    """
    # 백트래킹 예정
    global black
    if i == len(CCTV):
        black = min(black, N*M - obstacle - cnt)
        return
    # 카메라 종류 판단 후 경우의 수에 따른 회전 횟수 결정
    model = CCTV[i][0]  # model: 카메라 종류(1~5)
    for r in range(cases[model]):
        rotated_direction = list(map(lambda x: (x + r) % 4, direction[model]))  # 회전된 방향
        # 회전된 방향으로 탐색 시작 (반복문 이용)
        surveyed_areas = []
        for d in rotated_direction:
            ci, cj = CCTV[i][1]     # ci, cj: 카메라 위치
            while True:
                ni, nj = ci+delta[d][0], cj+delta[d][1]
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 6:
                    ci, cj = ni, nj
                    # 이미 조사한 칸이 아닌지 확인
                    if arr[ni][nj] != 0:
                        continue
                    arr[ni][nj] = 9
                    surveyed_areas.append((ni, nj))
                else:
                    break
        find_black(i+1, cnt+len(surveyed_areas))
        # 탐색된 위치 원상복구
        for area in surveyed_areas:
            si, sj = area
            arr[si][sj] = 0


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cases = {1: 4, 2: 2, 3: 4, 4: 4, 5: 1}  # CCTV 종류 별 경우의 수 개수
direction = {1: [1], 2: [1, 3], 3: [0, 1], 4: [0, 1, 3], 5: [0, 1, 2, 3]} # CCTV 종류 별 방향
delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# CCTV 체크
CCTV = []
obstacle = 0    # 사각지대 개수 셀 때 빼야하는 값(카메라, 벽 등)
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            obstacle += 1
            # CCTV 확인
            if arr[i][j] != 6:
                CCTV.append([arr[i][j], (i, j)])  # CCTV[num][0]: CCTV 종류, CCTV[num][1]: CCTV 위치

black = N*M     # 사각지대 개수
find_black(0, 0)
print(black)