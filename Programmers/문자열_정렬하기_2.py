def solution(my_string):
    answer = list(map(str, str(my_string)))
    for i in range(len(answer)):
        if answer[i].isupper() == True:
            answer[i] = answer[i].lower()
    answer.sort()
    return ''.join(answer)
