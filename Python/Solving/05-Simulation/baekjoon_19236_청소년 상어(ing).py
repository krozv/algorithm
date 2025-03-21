# 19236. 청소년 상어
"""
번호 1<= <=16자연수
두 물고기가 같은 번호 갖는 경우 없음
방향 8가지
청소년 상어 (0, 0)으로 들어감
물고기 먹음
물고기 이동
번호가 작은 물고기부터 순서대로 이동
한 칸 이동 가능
이동가능 칸: 빈칸, 다른 물고기가 있는 칸
이동 불가 칸: 상어있거나, 공간없는 곳
이동불가할 경우 방향 45도 반시계 회전
회전 후에도 이동 불가할 경우 이동안함
물고기가 다른 물고기 있는 칸으로 이동할 경우 서로의 위치 교환
물고기이동 완ㄹ료 -> 청소년 상어 이동
상어는 한번에 여러개 칸 이동 가능
이동하는 중에 지나가는 칸에 있는 물고기 안먹음
물고기 있는 칸으로만 이동 가능
이동불가할 경우 집으로 감

상어가 먹을 수 있는 물고기 번호의 합의 최댓값
"""
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

class Fish:
    def __init__(self, i, j, dir):
        self.i = i
        self.j = j
        self.dir = dir



def rotation(arr, shark, shark_dir, fish_dir):
    # 물고기 돌림
    fishes = []
    for i in range(4):
        for j in range(4):
            if arr[i][j] != 's':
                fishes.append([arr[i][j], i, j])
    fishes.sort(key=lambda x: x[0])
    print(fishes)
    for fish in fishes:
        fi, fj = fish[1], fish[2]
        cnt = 0
        while cnt < 8:
            ni, nj = fi+dir[fish_dir[arr[fi][fj]]][0], fj+dir[fish_dir[arr[fi][fj]]][1]
            if 0<=ni<4 and 0<=nj<4 and arr[ni][nj] != 's':
                print(arr[fi][fj], arr[ni][nj])
                arr[fi][fj], arr[ni][nj] = arr[ni][nj], arr[fi][fj]
                print(arr)
                break
            else:
                fish_dir[arr[fi][fj]] = (fish_dir[arr[fi][fj]] + 1) % 8
                cnt += 1
    # 상어 위치에 따른 possible_fish 추출
    possible_fish = []
    for k in range(1, 4):
        si, sj = shark
        ni, nj = si+dir[shark_dir][0]*k, sj+dir[shark_dir][1]*k
        if 0<=ni<4 and 0<=nj<4 and arr[ni][nj] != 0:
            possible_fish.append((ni, nj))
    return possible_fish


def eating_fish(eat, possible_fish, arr):
    if len(possible_fish) == 0:
        print(eat)
        return

    # 상어가 물고기 먹음
    for eaten_fish in possible_fish:
        si, sj = eaten_fish
        eat += arr[si][sj]
        shark_dir = fish_dir[arr[si][sj]]
        arr[si][sj] = 's'
        # 회전하러 보냄
        possible_fish = rotation(arr, eaten_fish, shark_dir, fish_dir)
        # 재귀 시작
        eating_fish(eat, possible_fish)
        # 회전 원상복귀
        eat -= arr[si][sj]
        # possible_fish = rotation(arr, shark_dir, fish_dir)


arr = [list(map(int, input().split())) for _ in range(4)]
arr1 = [[0]*4 for _ in range(4)]
fish_dir = {}
# 물고기 방향 저장
for i in range(4):
    for j in range(4):
        fish_dir[arr[i][j*2]] = arr[i][j*2+1]
        arr1[i][j] = arr[i][j*2]


# 방향번호~
dir = [0, (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
si, sj = 0, 0   # 초기 상어 좌표
eat = 0         # 먹은 물고기 번호

eating_fish(eat, [(si, sj)], arr1)