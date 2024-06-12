# 6019. 기차 사이의 파리
"""
거리 = 시간 X 속력
파리가 움직인 거리는?
"""
T = int(input())

for t in range(1, T+1):
    D, A, B, F = map(int, input().split())
    print(f'#{t} {F * D / (A + B)}')