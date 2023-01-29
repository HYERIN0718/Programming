while True:
    n = int(input())
    if n == 0:
        break
    if n < 10:
        print(n)
    while n >= 10:
        a = list(map(int, str(n)))
        b = 0

        for i in a:
            b += i
        if b < 10:
            print(b)
            break
        else:
            n = b
