n = 1460
count = 0

while n >= 10:
    if n >= 500:
        count += n //500
        n %= 500
    elif n >= 100:
        count += n //100
        n %= 100
    elif n >= 50:
        count += n //50
        n %= 50
    elif n >= 10:
        count += n //10
        n %= 10

print(count)
