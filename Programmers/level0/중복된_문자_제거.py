def solution(my_string):
    answer = ''
    arr = []
    arr_list = list(map(str, str(my_string)))
    
    for i in range(len(arr_list)):
        if arr_list[i] not in arr:
            arr.append(arr_list[i])
    answer = ''.join(arr)
    
    return answer
