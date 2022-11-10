T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    print("#%d" %test_case, end =' ')
    for i in range(n):
        print(arr[i], end=' ')
    print()
