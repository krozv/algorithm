def Counting_Sort(data, temp, k):
    '''
    data = [] 입력 배열 (0 to k)
    temp = [] 정렬된 배열
    counts = [] 카운트 배열
    '''
    counts = [0] * (k+1)
    for i in range(len(data)):
        counts(data[i]) = data[i]
