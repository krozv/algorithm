arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
# 코딩테스트용

nodes = [[] for _ in range(14)]
for i in range(0, len(arr), 2):
    parent_node = arr[i]
    child_node = arr[i+1]
    nodes[parent_node].append(child_node)

# 자식이 없다는 것을 표시하기 위해 None
for li in nodes:
    for _ in range(len(li), 2):
        li.append(None)


# 중위순회 구현
def inorder(nodeNum):
    if not nodeNum:
        return
    # 왼쪽으로 갈 수 있다면
    inorder(nodes[nodeNum][0])
    print(nodeNum, end=' ')
    inorder(nodes[nodeNum][1])


inorder(1)