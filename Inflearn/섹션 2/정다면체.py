import sys
sys.stdin=open("input.txt", "rt")

a, b = map(int, input().split())

# 나올 수 있는 수 만큼의 배열 크기 초기화하기
cnt = [0]*(a + b + 3)
aMax = 0

# 주사위 두 개를 던져서 나올 수 있는 수 모두 구하기
for i in range(1, a + 1):
    for j in range(1, b + 1):
        cnt[i + j] += 1

# 확률이 높은 숫자
for i in range(a + b + 1):
    if cnt[i] > aMax:
        aMax = cnt[i]

# 오름차순으로 출력
for i in range(a + b + 1):
    if cnt[i] == aMax:
        print(i, end=' ')
