import sys

def solve():
    try:
        N = int(sys.stdin.readline())
    except:
        return

    try:
        P = list(map(int, sys.stdin.readline().split()))
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
