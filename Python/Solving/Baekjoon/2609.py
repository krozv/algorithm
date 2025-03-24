# 2609. 최대공약수와 최소공배수
import sys
# sys.stdin = open("input.txt")
input = sys.stdin.readline


def divide(num):
    num_dict = {}
    
    for i in range(2, num//2+1):
        while num != 1:
            if num % i:
                break
            num //= i
            
            if i not in num_dict:
                num_dict[i] = 1
            else:
                num_dict[i] += 1
    
    if not num_dict and num != 1:
        num_dict[num] = 1
    return num_dict

def greatest(a_dict, b_dict):
    ans = 1
    
    for key, val in a_dict.items():
        if key not in b_dict:
            continue
        ans *= (key ** min(a_dict[key], b_dict[key]))

    return ans

def least(a_dict, b_dict):
    ans = 1
    
    for key, val in a_dict.items():
        ans *= (key ** max(val, b_dict.get(key, 1)))
        
    for key, val in b_dict.items():
        if key in a_dict:
            continue
        ans *= (key ** val)
    
    return ans

def solution():
    a, b = map(int, input().split())
    a_dict = divide(a)
    b_dict = divide(b)
    print(a_dict, b_dict)
    print(greatest(a_dict, b_dict))
    print(least(a_dict, b_dict))


if __name__ == "__main__":
    solution()