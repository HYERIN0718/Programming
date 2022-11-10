def solution(my_string):
    answer = 0
    arr = list(map(str, str(my_string)))
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    for i in range(len(arr)):
        if arr[i] in num:
            answer += int(arr[i])
    return answer
