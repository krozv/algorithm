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
def yammy_carrot(cnt, N):
    while True:
        boxes = []
        box = []
        min_carrot = N
        max_carrot = 0
        print(N // 3 + N % 3 - 1, round(N / 2))
        for i in range(31):
            if cnt[i] > 0:
                # 조건1. 한 상자에 N//2개를 초과하는 당근X
                print(i, len(box))
                if len(boxes) == 3:
                    box += [i] * cnt[i]
                elif len(box) + cnt[i] < N//3 + N%3 -1:
                    box += [i] * cnt[i]
                elif N//3 + N%3 -1 <= len(box) + cnt[i] < round(N/2):
                    box += [i] * cnt[i]
                else:
                    boxes += [box]
                    if len(box) < min_carrot:
                        min_carrot = len(box)
                    if len(box) > max_carrot:
                        max_carrot = len(box)
                    box = [i] * cnt[i]
        else:
            if len(box) < min_carrot:
                min_carrot = len(box)
            if len(box) > max_carrot:
                max_carrot = len(box)
            boxes += [box]
            return boxes, len(boxes), max_carrot-min_carrot


import sys
sys.stdin = open("sample_in.txt")
T = int(input())
for t in range(1, T+1):
    N = int(input())    # 당근 개수, 3 <= N <= 1000
    C = list(map(int, input().split()))     # 1 <= C <= 30
    cnt = [0] * 31
    # 당근 크기 별로 카운트를 센다
    for i in range(N):
        cnt[C[i]] += 1
    boxes, box_cnt, carrot = yammy_carrot(cnt, N)
    print(boxes)
    # if box_cnt == 3:
    #     re_boxes, box_cnt, re_carrot = yammy_carrot(cnt, (N//3 + N%3))
    #     print(re_boxes)
    #     if carrot > re_carrot:
    #         carrot = re_carrot
    #     print(f'#{t} {carrot}')
    # else:
    #     print(f'#{t} -1')
                # 조건2. 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장 -> 개수 차이 서류에 표시



        # 넘을 경우 새로운 리스트에 추가
        # N//2까지만 담고 이후로는 다음 리스트에 담음
        # 만족한다면 재정렬
            # N//3까지만 담음
