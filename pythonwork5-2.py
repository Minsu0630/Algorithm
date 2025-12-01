def solve():
    try:
        N = int(input())
    except:
        return

    try:
        P = list(map(int, input().split()))
    except:
        return

    P.sort()
    
    total_time = 0
    current_time = 0
    
    for time in P:
        current_time += time
        total_time += current_time
        
    print(total_time)

if __name__ == "__main__":
    solve()
