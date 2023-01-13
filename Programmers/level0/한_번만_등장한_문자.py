def solution(s):
    answer = list(map(str, str(s)))
    arr1 = [0] * 26
    arr2 = ''
    
    for i in answer:
        arr1[ord(i)-97] += 1
    
    for i in range(len(arr1)):
        if arr1[i] == 1:
            arr2 += chr(i+97)
        
    return arr2
