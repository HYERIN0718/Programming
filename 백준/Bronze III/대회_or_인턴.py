n, m, k = map(int, input().split())
cnt = 0

# 여학생 2명 + 남학생 1명 + 인턴쉽 k명
while n >= 2 and m >= 1 and n+m-3 >= k:
    n -= 2
    m -=1
    cnt += 1
print(cnt)
