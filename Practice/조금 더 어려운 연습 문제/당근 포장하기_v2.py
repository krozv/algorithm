# 당근 포장하기
"""
당근 대/중/소
조건1. 한 상자에 N//2개를 초과하는 당근X
조건2. 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장 -> 개수 차이 서류에 표시
N개의 당근
조건3. 같은 크기의 당근은 같은 상자에
포장 못하면 -1
"""
def yammy_carrot(cnt: [int], N: int, limit: int):
    while True:
        boxes = []
        box = []
        min_carrot = N
        max_carrot = 0
        for i in range(31):
            if cnt[i] > 0:
                # 박스 2개 채워지면 나머지 당근 모두 마지막 상자에 집어넣음
                if len(boxes) == 2:
                    box += [i] * cnt[i]
                # 박스에 넣을 수 있음? 조건1 만족함?
                elif cnt[i] < limit:
                    # 당근 넣기 최적화
                    if len(box) + cnt[i] < (N + 1) // 3:
                        box += [i] * cnt[i]
                    else:
                        for num in range((N+1)//3, limit):
                            if len(box) + cnt[i] == num:
                                box += [i] * cnt[i]
                                if len(box) < min_carrot:
                                    min_carrot = len(box)
                                if len(box) > max_carrot:
                                    max_carrot = len(box)
                                boxes += [box]
                                box = []
                                break

        else:
            # min, max 못 쓰니까
            if len(box) < min_carrot:
                min_carrot = len(box)
            if len(box) > max_carrot:
                max_carrot = len(box)
            # 마지막 박스 포장
            boxes += [box]
            return len(boxes), max_carrot - min_carrot


import sys
sys.stdin = open("sample_in.txt")

T = int(input())
for t in range(1, T+1):
    N = int(input())    # 당근 개수, 3 <= N <= 1000
    C = list(map(int, input().split()))     # 1 <= C <= 30
    cnt = [0] * 31
    limit = round(N/2)
    for i in range(N):
        cnt[C[i]] += 1

    # 최적화된 당근 포장
    box_cnt, carrot = yammy_carrot(cnt, N, limit)
    if box_cnt == 3:
        print(f'#{t} {carrot}')
    else:
        print(f'#{t} -1')

