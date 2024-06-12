# 16637. 괄호 추가하기
"""
길이가 N인 수식
0~9정수와 연산자 +, -, x
연산자 우선순위 동일
왼쪽 순서부터 계산
괄호 안에 들어있는 식은 먼저 계산
중첩 괄호 사용 불가

풀이방식
1.스택1 사용해서 연산결과 집어넣음
2.괄호가 존재하는 인덱스에 도착하면 -> 스택2에 해당 숫자 집어넣고 계산 후 꺼냄
-> 결과를 스택1에 추가
"""
def calculator(arr):
    stack = []
    stk = []
    for i in range(N+1):
        # i가 괄호안에서 진행해야 할 연산자 인덱스일 경우
        if i in arr or i-1 in arr:
            stk.append(exp[i])
        elif i-2 in arr:
            b = int(exp[i])
            op = stk.pop()
            a = int(stk.pop())
            if op == '+':
                c = a + b
            elif op == '-':
                c = a - b
            else:
                c = a * b
            stack.append(c)
        # 아닐 경우
        else:
            if len(stack) == 3:
                b = int(stack.pop())
                op = stack.pop()
                a = int(stack.pop())
                if op == '+':
                    c = a + b
                elif op == '-':
                    c = a - b
                else:
                    c = a * b
                stack.append(c)
            if i < N:
                stack.append(exp[i])
    return int(stack[0])



def combination(a, t, i):
    """
    a: 현재까지 포함된 조합 개수
    t: 마지막으로 포함된 요소
    i: 조합 개수
    인덱스는 0~N-1까지 존재
    """
    global max_val
    if a == i:
        val = calculator(lst)
        if max_val < val:
            max_val = val
        return
    for j in range(t, N, 2):
        if j not in lst and j-2 not in lst and j < N-1:
            lst.append(j)
            combination(a+1, j, i)
            lst.pop()


import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
exp = input()
# 괄호를 적절히 추가해서 결과 최댓값 출력
n = ((N-1)//3)  # 최대로 넣을 수 있는 괄호 개수
# 괄호가 존재할 인덱스 계산해야 함 -> 조합 개수,,, 개열받네
# 0개부터 n개까지 조합 존재
# i개의 조합에서 가능한 괄호 인덱스 위치는? 조건이 존재하는 조합이네
# [0, 1, 2, 3] 에서 차이가 1인 경우는 조합 내에 포함되지 않게 만들자 왜냐면
# 0~2 / 2~4 / 4~6 와 같이 짝수 인덱스 내에서 가능
# i개의 괄호
# 0~2 4~6
max_val = -2**31
lst = []
if n == 0:
    val = calculator(lst)
    if max_val < val:
        max_val = val
else:
    for i in range(n+1):
        combination(0, 0, i)
print(max_val)


