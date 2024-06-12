# 덱
from collections import deque

q = []
for i in range(10000):
    q.append(i)
print('append')
while q:
    q.pop(0)
print('end')

dq = deque()
for i in range(10000):
    dq.append(i)
print('append')
while dq:
    dq.popleft()
print('end')