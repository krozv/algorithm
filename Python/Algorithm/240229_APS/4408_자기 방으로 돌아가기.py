# 4408. 자기 방으로 돌아가기
"""
설계
1. 이동 방향이 달라지더라도 정답 결과는 같음
2. 아랫 방 사람을 모두 윗 방으로 이동 -> swap
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    room = [0] * 201
    info = []
    for _ in range(N):
        s, f = map(int, input().split())
        if s > f:
            s, f = f, s
        info.append(((s-1)//2, (f-1)//2))
    time = 0
    info.sort(key=lambda x: x[-1])
    # print(info)
    ### 여기 문제 ### 
    for s, f in info:
        if f >= 200:
            f = 199
        time = sum(room[s:f+1])
        room[f] += 1
    # print(room)
    print(f'#{t} {time+1}')

