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

print(medal_list)
medal_list.sort(key=lambda x: (-x[1], -x[2], -x[3]))
print(medal_list)
# K국가가 몇등인지?
cnt = 1
for medal_info in medal_list:
    
    idx, *prev = medal_info

    if idx == K:
        print('이거당')
