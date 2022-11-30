def solution(i, j, k):
    answer = 0

    for s in range(i, j + 1):
        a = list(map(str, str(s)))
        for l in range(len(a)):
            if a[l] == str(k):
                answer += 1  
    return answer
