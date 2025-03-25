# 1918. 후위 표기식
"""

"""
import sys
sys.stdin = open("input.txt", "r", encoding="UTF8")
input = sys.stdin.readline

def solution():
    expression = list(input().strip('\n'))
    char_stk = []
    oper_stk = []

    priority = {'*': 2, '-': 1, '+': 1, '/': 2}
    for char in expression:
        # print(oper_stk)
        if char in ['*', '-', '+', '/']:
            # 우선순위 고려
            while oper_stk and oper_stk[-1] != '(' and priority[oper_stk[-1]] >= priority[char]:
                char_stk.append(oper_stk.pop())
            oper_stk.append(char)
        elif char in ['(']:
            oper_stk.append(char)
        elif char in [')']:
            # '(' 괄호 나올 때까지 POP
            while oper_stk[-1] != '(':
                char_stk.append(oper_stk.pop())
            oper_stk.pop()
        else:
            char_stk.append(char)
    
    while oper_stk:
        char_stk.append(oper_stk.pop())

    print(''.join(char_stk))

if __name__ == "__main__":
    solution()