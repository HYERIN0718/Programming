import sys
sys.stdin=open("input.txt", "rt")

n = int(input())

# n까지 반복해야하므로 배열의 크기를 n + 1 만큼 초기화함
arr = [0] * (n + 1)
cnt = 0

for i in range(2, n + 1):
    
    # 처음 숫자인 2는 소수이므로 0값을 가지게 됨
    if arr[i] == 0:
        cnt += 1
        
        # if문 안의 for문 -> 값이 0인 인덱스의 배수 값에 1을 넣어야 하기 때문
        # range(i, n+1, i) -> i 만큼 증가 : i 배수 값 
        for j in range(i, n + 1, i):
            arr[j] = 1

print(cnt)
