# [baekjoon] 10799. 쇠막대기

## Data Structure

- stack

## Algorithm

- .

## How to solve

### Method

- 괄호의 모양에 따라 case를 분할해서 쇠막대기의 개수를 세었음
- '('일 경우 스택에 append 하여 잘린 쇠막대기의 개수를 파악함

### Constraint
1. 시간 복잡도
   - 1초 : 1,000,000,000
   - n <= 100,000
   - O(n)
2. 공간 복잡도

### Review
- 메모리: 32336 KB
- 시간: 64 ms
```python
# 10799. 쇠막대기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

string = list(input())
stack = []
prev = ''
cnt = 0
for char in string:
    # prev == ( and char == ) : 레이저
    if prev == '(' and char == ')':
        # stack 에서 pop
        stack.pop()
        # 남은 stack 길이만큼 cnt 증가
        cnt += len(stack)
    # prev == ) and char == ) : 조각 꺼내기
    if prev == ')' and char == ')':
        # stack 에서 pop
        stack.pop()
        cnt += 1
    # char == ( : 조각 넣기
    if char == '(':
        # stack에 append
        stack.append(char)
    prev = char
print(cnt)
```