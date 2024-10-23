# 7432. 디스크 트리
# tree node 만들기
class Node:
    def __init__(self):
        self.children = dict()


class Tree:
    def __init__(self):
        self.parent = Node()

    # 삽입
    def insert(self, string):
        curr_node = self.parent

        for word in string:
            # 자식이 없으면 생성
            if curr_node.children.get(word) is None:
                curr_node.children[word] = Node()

            # 자식이 있으면 이동
            curr_node = curr_node.children[word]

    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.parent

        for key, child in sorted(node.children.items()):
            print(" " * level + key)
            self.print_tree(child, level + 1)


import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())    # 전체 경로의 개수
tree = Tree()
for _ in range(N):
    string = input().strip("\n").split("\\")
    tree.insert(string)
tree.print_tree()

