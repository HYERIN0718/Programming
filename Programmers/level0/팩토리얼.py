def solution(n):
    answer = 0
    a = 1
    b = 0
    
    for i in range(1, 11):
        if a * i <= n:
            a = a * i
            b += 1
        else:
            break
    answer = b
    return answer
