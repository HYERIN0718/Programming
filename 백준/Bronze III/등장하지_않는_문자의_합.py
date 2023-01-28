n = int(input())
s = {"A", "B", "C", "D", "E","F","G","H","I","J","K","L","N","M","O","P","Q","R","S","T","U","V","W","X","Y","Z"}

for i in range(n):
    a = set(input())
    cnt = 0
    
    # set 형태는 뺄셈 가능
    b = s - a
    
    for j in b:
      
        # 중복 가능성이 있으므로 등장하지 않는 대문자를 더하는 방식이 정확함
        cnt += ord(j)
    print(cnt)
