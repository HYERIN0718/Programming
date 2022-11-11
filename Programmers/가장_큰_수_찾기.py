def solution(array):
    answer = []
    a = 0
    s = 0
    
    for i in range(len(array) - 1):
        if array[i] < array[i + 1]:
            a = array[i + 1]
            s = i + 1
        else :
            a = array[i]
            s = i
    answer.append(a)
    answer.append(s)

    return answer
