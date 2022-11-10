def solution(my_string):
    answer = []
    arr = list(map(str, str(my_string)))
    num = ['0','1','2','3','4','5','6','7','8','9']
    
    for i in range(len(arr)):
        if arr[i] in num:
            answer.append(int(arr[i]))
    answer.sort()
    return answer
