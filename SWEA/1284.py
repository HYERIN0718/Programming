T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    cost_A = P * W
    
    if W >= R:
        cost_B = Q + ((W-R) * S)
    elif R > W:
        cost_B = Q
        
        
    print("#%d" %test_case, min(cost_A, cost_B))
