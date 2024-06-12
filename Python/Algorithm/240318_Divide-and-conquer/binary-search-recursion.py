# 이진 검색
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 1. 정렬된 상태의 데이터
arr.sort()

# 이진 검색 - 재귀 함수 버전
def binarySearch(low, high, target):
    # 기저조건: 언제까지 재귀가 반복되어야 할까?
    if low > high:
        return -1
    # 다음 재귀 들어가기 전에 무엇을 해야할까?
    # -> 정답 판별
    mid = (low + high) // 2
    if target == arr[mid]:
        return mid

    # 다음 재귀 함수 호출 (파라미터)
    if target < arr[mid]:
        return binarySearch(low, mid-1, target)
    else:
        return binarySearch(mid+1, high, target)

    # 재귀 함수에서 돌아왔을 때 어떤 작업을 해야할까?
    # -> 이전 검색에서는 없음
