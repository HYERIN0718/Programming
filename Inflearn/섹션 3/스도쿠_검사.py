import sys
sys.stdin=open("input.txt", "rt")

def check(a):
  
    # 행, 열 한줄씩 1~9 맞는지 확인
    for i in range(9):
        ch1 = [0] * 10
        ch2 = [0] * 10
        for j in range(9):
            ch1[a[i][j]] = 1
            ch2[a[j][i]] = 1
        if sum(ch1) != 9 or sum(ch2) != 9:
            return False
          
    # 3x3칸씩 1~9 맞는지 확인
    for i in range(3):
        for j in range(3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]] = 1
            if sum(ch3) != 9:
                return False
    return True
  
    '''범위 수정
    # 3x3칸씩 1~9 맞는지 확인
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            ch3 = [0] * 10
            for k in range(3):
                for s in range(3):
                
                    # i와 j 범위를 9(3씩 이동)까지 설정하면 *3을 해주지 않아도 됨
                    ch3[a[i+k][j+s]] = 1
            if sum(ch3) != 9:
                return False
    return True '''

a = [list(map(int, input().split())) for _ in range(9)]
if check(a):
    print("YES")
else:
    print("NO")
