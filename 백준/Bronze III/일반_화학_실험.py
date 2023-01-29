a = []

while True:
    n = float(input())

    if n == 999:
        break
    a.append(n)


b = []
for i in range(len(a)-1):
    b.append(a[i+1] - a[i])

for x in b:
  
    # %.2f - 소수점 둘째자리까지 출력
    print('%.2f' %x)
