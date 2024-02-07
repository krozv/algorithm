# 당근 포장하기 - 나중에 풀기
"""
당근 대/중/소
조건1. 한 상자에 N//2개를 초과하는 당근X
조건2. 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장 -> 개수 차이 서류에 표시
N개의 당근
조건3. 같은 크기의 당근은 같은 상자에
포장 못하면 -1
포장할 수 있으며 각 사
"""
import sys
sys.stdin = open('carrot.txt', 'r')

T = int(input())
for t in range(1, T+1):
    print(t)
    N = int(input())
    carrots = list(map(int, input().split()))
    carrot_cnt = [0] * 31
    # 무게 별 carrot 몇 개?
    for carrot in carrots:
        carrot_cnt[carrot] += 1
    # 박스 포장 가능 여부 확인
    if max(carrot_cnt) > round(N/2):    # 박스 포장 불가
        print(-1)
    else:   # 박스 포장 가능
        boxes = [0]*3   # 박스 미리 접어놓음
        for i in range(31):      # 박스 포장 시작

            if sum(boxes) == N:
                break
            if carrot_cnt[i] + boxes[0] <= N//2:                    # 포장 가능
                if (N+1)//3 < carrot_cnt[i] + boxes[0] <= N//2:     # 걍 포장
                    boxes[1] += carrot_cnt[i]
                elif carrot_cnt[i] + boxes[0] <= (N+1)//3:          # 최적화 포장
                    boxes[0] += carrot_cnt[i]
            else:
                print(i)
                if carrot_cnt[i] + boxes[1] <= N//2:
                    print((N + 1) // 3, N // 2)
                    print(carrot_cnt[i] + boxes[1])
                    if (N+1)//3 < carrot_cnt[i] + boxes[1] <= N//2:  # 걍 포장
                        boxes[2] += carrot_cnt[i]
                    elif carrot_cnt[i] + boxes[1] <= (N+1)//3:  # 최적화 포장
                        boxes[1] += carrot_cnt[i]
                    else:
                        boxes[1] += carrot_cnt[i]
                else:
                    boxes[2] += carrot_cnt[i]
            print(boxes)

