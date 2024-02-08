'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def dfs(i, V):#시작 i, 마지막 V
    visited = [0]*(V+1)#visited, stack 생성 및 초기화
    st = []
    visited[i] = 1      #시작점 방문
    print(i)            #정점에서 할일
    while True:# 탐색
        #현재 방문한 정점에 인접하고 방문않나 정점w가 있으면
        for w in adjl[i]:
            if visited[w] == 0:
                st.append(i)    #push(i),i를 지나서
                i = w           #w에 방문
                visited[i] = 1
                print(w)
                break           #for w
        else:                   #for w, i에 남은 인접 정점이 없으면
            #스택이 비어있지 않으면(지나온 정점이 남아 있으면)
            if st:
                i = st.pop()
            else:    #스택이 비어있으면(출발점에서 남은 정점이 없으면)
                break #while True
    return

V, E = map(int, input().split())#V는
arr = list(map(int, input().split()))
#인접리스트
adjl = [[] for _ in range(V+1)] #adjl[i]행에는 i에 인접인 정점번호
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1) #방향이 없는 경우!

dfs(1, V)