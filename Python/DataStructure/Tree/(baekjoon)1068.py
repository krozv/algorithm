# 1068. 트리
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

cnt = 0
def count_node(node):
    global cnt
    if node == removed_node:
        return
    if not tree[node]:
        cnt += 1
        return
    if len(tree[node]) == 1 and tree[node][0] == removed_node:
        cnt += 1
        return
    for child in tree[node]:
        count_node(child)
    return

N = int(input())
arr = list(map(int, input().split()))
removed_node = int(input()) # 지워야하는 노드

tree = [[] for _ in range(N)]
root = None

for child, parent in enumerate(arr):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)

count_node(root)
print(cnt)

