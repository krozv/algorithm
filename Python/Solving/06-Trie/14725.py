# 개미굴
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

class Node:

    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, foods):
        node = self.root

        for food in foods:
            #print(node.val)
            if food not in node.children.keys():
                node.children[food] = Node(food)
            node = node.children[food]
        node.is_end = True
    
    def print_tree(self, node=None, cnt=0):
        if not node:
            node = self.root
        if node.val:
            print(f"{'-'*2*(cnt-1)}{node.val}") 
        for child in sorted(node.children.keys()):
            self.print_tree(node.children[child], cnt=cnt+1)


def solution():
    n = int(input())
    trie = Trie()
    for _ in range(n):
        _, *foods = input().split()

        trie.insert(foods)
    
    trie.print_tree()



if __name__ == "__main__":
    solution()