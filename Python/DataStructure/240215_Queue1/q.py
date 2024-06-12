# 선형 큐
# 큐 생성
N = 10
q = [0] * 10
front = rear = -1

# 삽입: enQueue(item)
rear += 1
q[rear] = 10

rear += 1
q[rear] = 20

rear += 1
q[rear] = 30

# 삭제: deQueue()
while front != rear:
    front += 1
    print(q[front])
#