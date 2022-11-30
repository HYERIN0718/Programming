def solution(my_string):
    answer = ''
    arr = ['a', 'e', 'o', 'i', 'u']
    arr_list = list(map(str, str(my_string)))
    list_answer = []
    
    for i in range(len(arr_list)):
        if arr_list[i] not in arr:
            list_answer.append(arr_list[i])
    answer = ''.join(list_answer)
    return answer
