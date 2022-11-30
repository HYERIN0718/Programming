def solution(cipher, code):
    arr = list(map(str, str(cipher)))
    answer = []
    
    for i in range(code-1, len(arr), code):
        answer += arr[i]
        
    return ''.join(answer)
