# 오픈채팅방
import sys
input = sys.stdin.readline
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    answer = []
    id_dict = {}
    temp = []
    # record를 공백 기준으로 분리
    records = []
    for i in record:
        records.append(i.split())

    # answer에 유저아이디와 출입여부 append
    for info in records:
        if info[0] == 'Enter':
            temp.append([info[0], info[1]])
            id_dict[info[1]] = info[2]
        elif info[0] == 'Leave':
            temp.append([info[0], info[1]])
        else:
            id_dict[info[1]] = info[2]
    # 딕셔너리에 아이디: 닉네임으로 저장
    # 끝까지 저장 후 answer의 아이디를 닉네임으로 변경
    for i in range(len(temp)):
        if temp[i][0] == 'Enter':
            answer.append(f'{id_dict[temp[i][1]]}님이 들어왔습니다.')
        else:
            answer.append(f'{id_dict[temp[i][1]]}님이 나갔습니다.')
    return answer


solution(record)