# 삼성시의 버스 노선.. 나도 삼성..가고 싶...
'''
정류장 1~5000개
T 테스트 케이스
N 버스 노선 1 <= N <= 500
Ai, Bi 1 <= A <= B <= 5000 버스가 가는 정류장
Aj, Bj
...
P 정류장 개수
C 정류장 넘버 하나씩
'''
import sys
sys.stdin = open('input_bus.txt', 'r')
T = int(input())
for t in range(1, T+1):
    N = int(input())
    bus_line = [0] * 5001 # 정류장 넘버 별로 몇 개의 버스가 갈 것인지 셀 것임
    for n in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus_line[i] += 1
    P = int(input())
    bus_stops = [int(input()) for _ in range(P)]
    for idx in range(P):
        bus_stops[idx] = bus_line[bus_stops[idx]]
    print(f'#{t}', end=' ')
    print(*bus_stops)