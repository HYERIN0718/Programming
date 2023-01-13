def solution(array, n):
    answer = 0 
    lt = 100
    res = 0
    
    for i in range(len(array)):
        if abs(array[i] - n) < lt:
            lt = abs(array[i] - n)
            answer = array[i]
            res = i
        elif abs(array[i] - n) == lt:
            if array[i] < answer:
                answer = array[i]
                 
    return answer
