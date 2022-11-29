def solution(order):
    answer = 0
    arr_list = list(map(str, str(order)))
    
    for i in range(len(arr_list)): 
        if arr_list[i] == "3" or arr_list[i] == "6" or arr_list[i] == "9":
            answer += 1

    return answer
