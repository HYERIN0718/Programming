while True:
    a = sorted(list(map(int, input().split())))
    if a[0] == a[1] == a[2] == 0:
        break
    if a[0] + a[1] <= a[2]: # 세 변의 길이가(2, 2, 8)일 때 삼각형이 만들어지지 않으므로 Invalid를 출력해서 오류 방지
        print("Invalid")
    elif a[0] == a[1] == a[2]:
        print("Equilateral")
    elif a[0] == a[1] or a[1] == a[2] or a[2] == a[0]:
        print("Isosceles")
    else:
         print("Scalene")
