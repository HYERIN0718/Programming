T = int(input())
cal = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

for test_case in range(1, T + 1):
    a, b, c, d = map(int, input().split())
    answer = 0
    e = 0
    f = 0
    
    if a == c:
        answer = d - b + 1
    elif c > a:
        for i in range(1, c):
            e += cal.get(i)        
        for i in range(1, a):
            f += cal.get(i)
        answer = (e + d) - (f + b) +1
        
        
    print("#%d" %test_case, answer)
