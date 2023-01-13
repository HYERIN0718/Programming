def solution(numbers, direction):
    answer = list(map(int, numbers))
    
    if direction == "right":
        answer.insert(0, answer.pop())
    else:
        answer.append(answer.pop(0))
    return answer
