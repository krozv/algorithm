# 정렬
arr = [[2, 2], [1, 3], [1, 2], [3, 1]]
# x, y 좌표를 정렬 -> y에 대해서 오름차순 정렬, y가 같은 경우 x가 작은 순
arr.sort(key=lambda x: (x[1], x[0]))
print(arr)

'''
or
'''
arr = [[2, 2], [1, 3], [1, 2], [3, 1]]
arr.sort(key=lambda x: x[0])    # 우선순위가 낮은 키부터 정렬
arr.sort(key=lambda x: x[1])
print(arr)