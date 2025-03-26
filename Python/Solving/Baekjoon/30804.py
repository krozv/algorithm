# 30804. 과일 탕후후
import sys
sys.stdin = open("input.txt", "rt", encoding="UTF8")
input = sys.stdin.readline
DEBUG = False

def solution():
    N = int(input()) # 과일의 개수 N
    fruits = list(map(int, input().split()))
    
    s, e = 0, 0
    cnt = 0
    tang = []
    tang.append(fruits[0])

    # 전체 과일 종류가 2가지 이하일 때
    res = len(set(fruits))

    if res <= 2:
        return res
    
    while s < (N-1):
        # back tracking
        if cnt >= (len(tang)+N-s-1):
            return cnt
        # print(f"s: {s}, e: {e}, tang: {tang}")
        temp = set(tang)
        temp.add(fruits[s+1])

        # s가 이동 가능한 경우
        if len(temp) <= 2:
            # s 이동하고, tang 뒤에 넣는다
            s += 1
            tang.append(fruits[s])
        # s가 이동 불가능한 경우
        else:
            # e를 이동하고, tang popleft 한다.
            e += 1
            tang = tang[1:]
        
        # tang 길이 변화가 있을 경우, 즉, tang 길이가 cnt보다 증가한 경우 업데이트한다.
        if cnt < len(tang):
            cnt = len(tang)
    
    return cnt

if __name__ == "__main__":
    print(solution())