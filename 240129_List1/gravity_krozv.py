# Gravity 연습 문제
'''
가장 큰 낙차 리턴
N 높이
num_list 각 상자 개수
'''
N = 9
num_list = [7, 4, 2, 0, 0, 6, 0, 7, 0]
'''
i > i+1일 경우 count +1
i =< i+1 stop
'''
# krozv
max_count = 0
for i in range(N-1):
    count = 0
    for j in range(i+1, N):
        if num_list[i] <= num_list[j]:
            break
        else:
            count += 1
    if max_count < count:
        max_count = count
print(max_count)

# solution
max_count = 0
for i in range(N-1):
    count = 0
    for j in range(i+1, N):
        if num_list[i] > num_list[j]:
            count += 1
    if max_count < count:
        max_count = count
print(max_count)