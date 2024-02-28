# 베이비진 게임
"""
0~9 숫자 카드 4세트 중 6개의 카드 선정
run: 연속인 숫자가 3개 이상
triplet: 같은 숫자가 3개 이상
6장 다 안채워도 run, triplet이 되면 승자
승자 출력 1, 2
무승부 0
"""
def test(card):
    """
    card: 판단할 카드 array
    n: 현재 있는 카드 수 - 1
    """
    bit = [0] * 10
    cnt = [0] * 10

    # 카드 개수 셈
    for c in card:
        bit[c] = 1
        cnt[c] += 1
    bit = int(''.join(list(map(str, bit))), 2)

    run = False
    triplet = False

    # run 판단
    for i in range(9):
        if bit & (0b111 << i) == (0b111 << i):
            run = True
            break

    # triplet 판단
    for i in range(10):
        if cnt[i] == 3:
            triplet = True
            break

    if run or triplet:
        return True
    else:
        return False


import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    A = []
    B = []

    for i in range(6):
        A.append(arr[i*2])
        B.append(arr[i*2+1])
        if i >= 2:
            result_A = test(A)
            result_B = test(B)
            if result_A or result_B:
                if result_A:
                    print(f'#{t} 1')
                else:
                    print(f'#{t} 2')
                break
    else:
        print(f'#{t} 0')