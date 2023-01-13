def solution(rsp):
    answer = []
    
    for i in range(len(rsp)):
        if rsp[i] == "2" :
            answer.append("0")
        elif rsp[i] == "5" :
            answer.append("2")
        else:
            answer.append("5")
    
    return ''.join(answer)
