s = list(map(int, input().split()))
s.sort()
a = list(input())

for i in a:
    if i == 'A':
        print(s[0], end= ' ')
    elif i == 'B':
        print(s[1], end= ' ')
    else:
        print(s[2], end= ' ')
