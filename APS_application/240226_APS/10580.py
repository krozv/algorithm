# 10580. 전봇대
"""

"""

def get_result():
    size = len(arr)
    cnt = 0
    for i in range(size):
        for tar in range(i):
            i_a, i_b = (arr[i][0], arr[i][1])
            tar_a, tar_b = (arr[tar][0], arr[tar][0])
            if i_b < tar_b:
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    for n in range(N):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x: x[0])
    result = get_result()
    print(result)