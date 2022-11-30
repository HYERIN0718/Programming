def solution(num_list, n):
    answer = []
    a = len(num_list)//n

    for i in range(a):
        answer.append(num_list[n*i:n*(i+1)])
        
    return answer
