import sys
sys.stdin=open("input.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
count = 0

# 방향키
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1행과 마지막 행에 [0] 배열 삽입
a.insert(0, [0]*n)
a.append([0]*n)

# 각 행과 열 맨앞, 맨뒤에 0 삽입
for i in range(n+2):
    a[i].insert(0, 0)
    a[i].append(0)

# 상하좌우 보다 큰 수 찾기
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            count += 1
print(count)
