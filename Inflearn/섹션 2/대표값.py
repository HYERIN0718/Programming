import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

ave = round(sum(a) / n)
aMin = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < aMin :
        aMin = tmp
        score = x 
        res = idx + 1
    elif tmp == aMin:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)
