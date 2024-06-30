# [baekjoon] 1068. 트리

## Data Structure

- Tree

## Algorithm

- 재귀

## How to solve

### Method

- tree 배열에 자식 노드를 append
- root 부터 재귀를 하면서 리프인지 아닌지 확인

### Constraint
1. 시간 복잡도
   - O(n)
2. 공간 복잡도

### Review
- 메모리: 31120 KB
- 시간: 44 ms
```python
# 1068. 트리
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

cnt = 0
def count_node(node):
    global cnt
    # 노드가 제거한 노드일 경우 return
    if node == removed_node:
        return
    # 리프 노드일 경우
    if not tree[node]:
        cnt += 1
        return
    # 자식 노드가 제거한 노드이고, 자식 노드의 개수 == 1 -> 리프 노드
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
```