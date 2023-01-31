def Binary(x):
    if x >= 1:
        Binary(x // 2 )
        print(x%2, end='')

if __name__=="__main__":
    n = int(input())
    Binary(n)
