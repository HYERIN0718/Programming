def solution(num, k):
    answer = 0
    num_list = list(map(int, str(num)))
    
    for i in range(len(num_list)):
        if num_list[i] == k:
            answer = i + 1
            break
        else:
            answer = -1
    return answer
