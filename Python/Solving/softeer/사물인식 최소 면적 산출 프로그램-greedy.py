# 사물인식 최소 면적 산출 프로그램
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')


def calculated_area(arr):
    x_min, x_max = arr[0][0], arr[0][0]
    y_min, y_max = arr[0][1], arr[0][1]
    for x, y in arr:
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    area = (x_max - x_min) * (y_max - y_min)
    return area


def f(n, a):
    """
    :param n: 선택한 점 개수
    :param a: 현재까지 넓이
    """
    global area
    if n == K+1:
        if area > a:
            area = a
        return

    if a >= area:
        return

    for dot in color[n]:
        dot_lst.append(dot)
        a = calculated_area(dot_lst)
        f(n+1, a)
        dot_lst.pop()


N, K = map(int, input().split())
color = {}
for _ in range(N):
    x, y, k = map(int, input().split())
    if color.get(k):
        color[k].append((x, y))
    else:
        color[k] = deque()
        color[k].append((x, y))

print(color)
dot_lst = []
area = 2000 * 2000
f(1, 0)
print(area)