import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

tc = int(input())
for t in range(tc):
    word = list(input().strip('\n'))
    flag = False
    head = Node(None)
    node = head

    for char in word:
        if char == '<':
            if node.prev is not None:
                node = node.prev
        elif char == '>':
            if node.next is not None:
                node = node.next
        elif char == '-':
            if node != head:
                prev_node = node.prev
                prev_node.next = node.next
                if node.next is not None:
                    node.next.prev = prev_node
                node = prev_node

        else:
            new_node = Node(char)
            new_node.prev = node
            new_node.next = node.next
            if node.next is not None:
                node.next.prev = new_node
            node.next = new_node
            node = new_node

    result = ""
    curr_node = head.next
    while curr_node is not None:
        result += curr_node.value
        curr_node = curr_node.next
    print(result)