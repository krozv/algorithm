# 컨테이너 운반
"""
N개의 컨테이너 M대의 트럭, A도시 -> B도시
트럭당 한 개의 컨테이너
트럭의 적재용량을 초과하는 컨테이너 운반 불가
최대 M대의 트럭이 편도로 한 번만 운영
옮겨진 전체 화물의 무게 출력
화물 안실어도 됨. 남는 화물 있어도 괜찮
컨테이너 한 개도 못옮기면 0
"""
import sys
sys.stdin = open('input.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())    # N: 컨테이너 개수, M: 트럭 대수
    w_lst = list(map(int, input().split()))
    t_lst = list(map(int, input().split()))
    w_lst.sort(reverse=True)
    t_lst.sort(reverse=True)
    cnt = 0
    for i in range(M):
        for j in range(N):
            if t_lst[i] and w_lst[j] and t_lst[i] >= w_lst[j]:
                cnt += w_lst[j]
                t_lst[i] = 0
                w_lst[j] = 0
                break
            else:
                w_lst[j] = 0
    print(f'#{t} {cnt}')

