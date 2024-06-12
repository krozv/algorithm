# 3665. 최종 순위
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

T = int(input())
for t in range(1, T+1):
    n = int(input()) # 팀의 수
    team = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    degree = [0] * (n+1)

    # graph로 변경
    for i in range(n-1):
        graph[team[i]].append(team[i+1])
        degree[team[i+1]] += 1

    print(graph)
    print(degree)

    m = int(input())    # 변경된 순위
    for i in range(m):
        a, b = map(int, input().split())
