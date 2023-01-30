while True:
    try:
        n, m, k = map(int, input().split())
        print(max(m-n, k-m) - 1 )
    except:
        break

# 내가 푼 답
'''while True:
    try: 
        n, m, k = map(int, input().split())
        if abs(m-n) <= abs(k-m):
            print(abs(k-m)-1)
        else:
            print(abs(m-n)-1)
    except:
        break '''
