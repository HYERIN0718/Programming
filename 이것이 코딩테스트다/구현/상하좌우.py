n = int(input())
arr = list(map(str, input().split()))
first = 1
second = 1

for x in arr:
    if x == 'R':
       if second < n:
           second += 1
    elif x == 'L':
        if second > 1:
            second -= 1
    elif x == 'U':
        if first > 1:
            first -= 1
    elif x == 'D':
        if first < n:
            first += 1

print(first, second)
