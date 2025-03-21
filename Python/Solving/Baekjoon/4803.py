# 4803. 트리
"""
그래프가 주어졌을 때, 트리의 개수를 세는 프로그램
"""
import sys
from collections import deque
sys.stdin = open("./input.txt")
input = sys.stdin.readline


# union끼리 묶음
def find_union(adj):
    result = []
    n = len(adj)
    visited = [0] * n
    # print(n)
    for i in range(1, n):
        # print('i: ', i)
        if visited[i]:
            continue

        union = [i]
        for node in adj[i]:
            q = deque()
            q.append(node)
            while q:
                # print(q)
                node = q.popleft()
                visited[node] = 1
                if node in union:
                    continue
                union.append(node)
                
                for next in adj[node]:
                    q.append(next)

        result.append(union)

    return result

# 묶은 union을 보고 tree인지 아닌지 판단
def find_tree(union, n, adj):
    tree = 0
    for graph in union:
        node = graph[0]
        visited = [0] * n
        edge = 0
        
        for node in graph:
            edge += len(adj[node])
        
        if len(graph) - (edge//2) == 1:
            tree += 1
    return tree

def solution():
    tc = 1
    while True:
        # n: 정점의 개수, m: 간선의 개수
        n, m = map(int, input().split())

        if n == 0 and m == 0: break
        
        adj = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b = map(int, input().split())
            adj[a].append(b)
            adj[b].append(a)
        # print(adj)
        union = find_union(adj)
        number = find_tree(union, n+1, adj)
        match (number):
            case 0: print(f"Case {tc}: No trees.")
            case 1: print(f"Case {tc}: There is one tree.")
            case _: print(f"Case {tc}: A forest of {number} trees.")

        tc += 1

if __name__ == "__main__":
    solution()
