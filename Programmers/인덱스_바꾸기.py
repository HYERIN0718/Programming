def solution(my_string, num1, num2):
    arr = list(map(str, str(my_string)))
    a = arr[num1]
    b = arr[num2];
    
    arr[num1] = b
    arr[num2] = a
    
    return ''.join(arr)
