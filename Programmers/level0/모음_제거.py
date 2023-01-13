def solution(my_string):
    answer = ''
    
    arr = list(map(str, str(my_string)))
    
    for i in range(len(arr)):
        if arr[i] not in 'aeiou':
            
            # 문자열 덧셈 가능
            answer += arr[i]
    return answer
