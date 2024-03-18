# 이진 검색
arr = [324, 32, 22114, 16, 48, 93, 422, 21, 316]

# 1. 정렬된 상태의 데이터
arr.sort()

# 2. 이진 검색 - 반복문 버전
def binary_search(target):
    # 제일 왼쪽, 오른쪽 인덱스 구하기
    low = 0
    high = len(arr)-1

    # 해당 숫자를 찾으면 종료
    # 더 이상 쪼갤 수 없을 때까지
    while low <= high:
        mid = (low + high) // 2

        # 가운데 숫자가 정답이면 종료
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1