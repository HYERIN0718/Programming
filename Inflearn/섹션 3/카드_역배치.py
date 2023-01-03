import sys
sys.stdin=open("input.txt", "rt")

# 20개의 인덱스를 가진 배열 생성
arr = list(range(21))

for _ in range(10):
    a, b = map(int, input().split())
    
    # (b-a+1)//2 : 숫자 교환 횟수 -> +1을 해주어야 짝수 횟수 교환가능
    for i in range((b-a+1) // 2):
        # 배열 값 교환 
        arr[a+i], arr[b-i] = arr[b-i], arr[a+i]

# 배열의 맨 앞 인덱스의 값 제거
arr.pop(0)

for j in arr:
    print(j, end=' ')
