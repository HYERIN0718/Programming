def solution(before, after):
    answer = 0
    before_list = list(map(str, str(before)))
    after_list = list(map(str, str(after)))
    arr = []
    
    for i in range(len(before_list)):
        if before_list[i] in after_list:
            after_list.remove(before_list[i])

    if len(arr) == len(after_list):
        answer = 1
    else:
        answer = 0
    return answer
