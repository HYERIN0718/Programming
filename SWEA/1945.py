T = int(input())
for test_case in range(1, T + 1):
    a = 0; b = 0; c = 0; d = 0; e = 0;
    case = int(input())
    while case % 2 == 0 :
        case = case / 2 
        a += 1;
    while case % 3 == 0:
        case = case / 3
        b += 1;
    while case % 5 == 0:
        case = case / 5
        c += 1;
    while case % 7 == 0:
        case = case / 7
        d += 1;
    while case % 11 == 0:
        case = case / 11
        e += 1;
    

    print("#%d" %test_case, a, b, c, d, e )
