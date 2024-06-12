# 2747. 피보나치 수 (DP 필수문제 #01)

[1] 시각적으로 접근 -> 규칙성 찾기

[2] dp[] table 정의, dp[i]

[3] 초기값 설정, 반복처리

dp[i]: i번째 피보나치 수 (dp[i-1] + dp[i-2])

```python
n = int(input())
dp = [0] * (n+1)
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n])
```