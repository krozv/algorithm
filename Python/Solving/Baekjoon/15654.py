# 15654. N과 M (5)
import sys
sys.stdin = open('input.txt', 'rt', encoding='UTF8')
input = sys.stdin.readline
debug = True

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(res, n):
    """
    numbers 중에서 m개의 숫자를 골라서 출력
    res: 출력할 수열을 담은 리스트
    n: 현재 res 안에 들어있는 숫자의 개수
    """
    global M, numbers

    if n == M:
        print(' '.join(map(str, res)))
        return
    
    for number in numbers:
        if not res or number not in res:
            new_res = []
            new_res.extend(res)
            new_res.append(number)
            dfs(new_res, n+1)


if __name__ == "__main__":
    dfs([], 0)