# 진법 변환
"""
input된 값을 진법 변환하여 출력
"""
arr = [[0]*3 for _ in range(16)]
print(0x11)
for i in range(16):
    arr[i][0] = bin(i)
    arr[i][1] = i
    arr[i][2] = hex(i)
test = list(map(int, input()))
print(test)
for num in test:
    pass