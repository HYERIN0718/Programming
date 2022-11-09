T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    k = []
    
    if n > m:
        for i in range(0, n - m + 1):        
            s = 0
            for j in range(m):
                s += A[j + i] * B[j]
            k.append(s)
    elif n < m:
        for i in range(m - n + 1):
            s = 0
            for j in range(n):
                s += A[j] * B[j + i]
            k.append(s)
            
    print("#%d" %test_case, max(k))
