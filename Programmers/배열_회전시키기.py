def solution(numbers, direction):
    answer = []
    
    if direction == "left":
        s = numbers[0]
        del numbers[0]
        numbers.insert(len(numbers), s)
    elif direction == "right":
        s = numbers[len(numbers) - 1]
        del numbers[len(numbers) - 1]
        numbers.insert(0, s)
    return numbers
