def solution(n):
    answer = 0
    arr = []
    
    for i in range(1, n + 1):
        a = []
        for j in range(1, i + 1):
            if i % j == 0:
                a.append(j)
        if len(a) >= 3:
            arr.append(i)
    answer = len(arr)
    return answer
