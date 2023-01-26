a, b = map(int, input().split())
n = int(input())

hour = (b+n) // 60
min = (b+n) % 60

if b + n >= 60:
    a = a + hour
    if a >= 24:
        a = a - 24
    print(a, min)
else:
    if a >= 24:
        a = hour - 24
    print(a, b+n)
