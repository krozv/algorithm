# 올림픽
'''
1. 금메달 수가 더 많은 나라
2. 금메달 수 같으면 -> 은메달 수
3. 은메달 수 같으면 -> 동메달 수
'''
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# N: 국가의 수
# K: 등수를 알고 싶은 국가
N, K = map(int, input().split())
medal_dict = {}
medal_list = []
for i in range(N):
    medal_list.append(list(map(int, input().split())))

    # _, *medal = map(int, input().split())
    # medal_dict[i] = medal

medal_list.sort(key=lambda x: (-x[1], -x[2], -x[3]))
# K국가가 몇등인지?
cnt = 1
prev = medal_list[0][1:]
for idx, medal_info in enumerate(medal_list):
    country, *medal = medal_info
    if prev == medal:
        pass
    else:
        cnt = idx + 1
    prev = medal
    if country == K:
        print(cnt)
        break