# binary search
def binary_search(arr, N, key):
    # 구간 초기화
    start = 0
    end = N-1
    while start <= end:                 # 검색 구간이 유효하면 반복
        middle = (start+end) // 2       # 중앙원소 인덱스
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            end = middle - 1
        else:
            start = middle + 1
    return -1