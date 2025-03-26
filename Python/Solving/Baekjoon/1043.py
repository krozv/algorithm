# 1043. 거짓말
import sys
sys.stdin = open("input.txt", "rt", encoding="UTF8")
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split()) # N: 사람의 수, M: 파티의 수
    truth = list(map(int, input().split()))
 
    adj = [[] for _ in range(N+1)] # 인접리스트

    # truth 처리
    true_people = None
    if len(truth) > 1:
        _, *true_people = truth
        print(true_people)
    else:
        true_people = None
        return M
    
    for _ in range(M):
        people = list(map(int, input().split()))
        _, *party_people = people
        for person in party_people:
            temp = []
            temp.extend(party_people)
            temp.remove(person)
            adj[person].extend(temp)
        
    print(adj)
    known = [0] * (N+1)
    for person in true_people:
        if known[person]: continue
        known[person] = 1
        




if __name__ == "__main__":
    solution()