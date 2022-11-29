def solution(numbers):
    answer = 0
    arr = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            a = numbers[i] * numbers[j]
            arr.append(a)
    
    answer = max(arr)    
    return answer
