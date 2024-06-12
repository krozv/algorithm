"""
목표
1. 이모티콘 플러스 서비스 가입자 최대한 증가
2. 이모티콘 판매액 증가
조건
1. 각 사용자들은 일정 비율 이상 할인하는 이모티콘 모두 구매
2. 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매를 모두 취소하고 이모티콘 플러스 서비스 가입

"""
from itertools import product

def solution(users, emoticons):
    answer = []
    print(len(users))
    sale = [10, 20, 30, 40]
    print(list(product(sale, repeat=2)))
    print(users)
    for
    return answer


users1 = [[40, 10000], [25, 10000]]
emoticons1 = [7000, 9000]
# result1 = [1, 5400]

users2 = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons2 = [1300, 1500, 1600, 4900]
# result2 = [4, 13860]

solution(users1, emoticons1)
