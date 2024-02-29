# 두 전구
"""
출력을 한 번에 내보내는 식으로 진행해야 시간 초과가 나지 않음
"""
import sys
sys.stdin = open('input.txt', 'r')
# 두 전구
T = int(input())
test = []
for t in range(1, T+1):
    A, B, C, D = map(int, input().split())
    lst = [(A, B), (C, D)]
    lst.sort(key=lambda x: x[-1])
    if lst[0][0] > lst[1][0]:
        time = lst[0][1] - lst[0][0]
    else:
        time = lst[0][1] - lst[1][0]
    if time < 0:
        time = 0
    test.append(time)
for idx, time in enumerate(test):
    print(f'#{idx+1} {time}')