# 당근 포장하기
"""
당근 대/중/소
조건1. 한 상자에 N//2개를 초과하는 당근X
조건2. 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장 -> 개수 차이 서류에 표시
N개의 당근
조건3. 같은 크기의 당근은 같은 상자에
포장 못하면 -1
포장할 수 있으며 각 사
"""
def yammy_carrot(cnt, N, limit):
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
                elif len(box) + cnt[i] < limit:

                    box += [i] * cnt[i]
                # 새 박스 꺼내자
                elif cnt[i] < limit:
                    if len(box) > 0:
                        # min, max 못 쓰니까..
                        if len(box) < min_carrot:
                            min_carrot = len(box)
                        if len(box) > max_carrot:
                            max_carrot = len(box)
                        boxes += [box]
                    box = [i] * cnt[i]
        else:
            # min, max 못 쓰니까..2
            if len(box) < min_carrot:
                min_carrot = len(box)
            if len(box) > max_carrot:
                max_carrot = len(box)
            # 마지막 박스 포장
            boxes += [box]
            return boxes, len(boxes), max_carrot-min_carrot


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

    # 처음 당근 포장 - 최적화X. 당근 포장 가능 여부 판별용
    boxes, box_cnt, carrot = yammy_carrot(cnt, limit, limit)

    # 최적화된 당근 포장 으쌰으쌰
    if box_cnt == 3:
        for j in range(round(N/2)-1, (N+1)//3-1, -1):
            re_boxes, box_cnt, re_carrot = yammy_carrot(cnt, j, limit)
            if carrot > re_carrot:
                carrot = re_carrot
        print(f'#{t} {carrot}')
    else:
        print(f'#{t} -1')