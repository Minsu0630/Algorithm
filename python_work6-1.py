import sys

def solve():
    board = sys.stdin.readline().strip()
    
    # 간편한 치환법: AAAA를 먼저 채우고, 남은 X를 BB로 채움
    board = board.replace("XXXX", "AAAA")
    board = board.replace("XX", "BB")
    
    # 여전히 X가 남아있다면 덮을 수 없는 부분이 있다는 뜻
    if 'X' in board:
        print("-1")
    else:
        print(board)

solve()
