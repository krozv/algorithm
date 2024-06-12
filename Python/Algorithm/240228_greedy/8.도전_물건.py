# 도전
"""
0-1 Knapsack 문제
그리디로 접근: 가격/kg이 높은 순으로 가져감 -> but greedy로 해결 불가
"""
"""
Fractional Knapsack 문제 -> 그리디로 접근 가능
"""
n = 3
target = 30
things = [(5, 50), (10, 60), (20, 140)]

things.sort(key=lambda x:(x[1]/x[0]), reverse=True)

sum = 0
for kg, price in things:
    per_price = price / kg

    if target < kg:
        sum += target * per_price
        break
    sum += price
    target -= kg

print(int(sum))
