import math

def check_win(b):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    for x,y,z in w:
        if b[x] == b[y] == b[z] != 0:
            return b[x]
    return 0 if 0 not in b else None

def selection(b, p):
    r = check_win(b)
    if r is not None:
        return r
    vals = []
    for i in range(9):
        if b[i] == 0:
            b[i] = p
            vals.append(selection(b, -p))
            b[i] = 0
    return max(vals) if p == 1 else min(vals)

def best_move(b):
    moves = []
    for i in range(9):
        if b[i] == 0:
            moves.append((selection(b[:i] + [1] + b[i+1:], -1), i))
    return max(moves)[1]

def print_board(b):
    s = {1:'X', -1:'O', 0:' '}
    for i in range(0,9,3):
        print(f"{s[b[i]]}|{s[b[i+1]]}|{s[b[i+2]]}")
        if i < 6:
            print("-----")

board = [0]*9
player = 1

while True:
    print_board(board)
    out = check_win(board)
    if out is not None:
        print("X wins!" if out == 1 else "O wins!" if out == -1 else "Tie!")
        break
    if player == 1:
        board[best_move(board)] = 1
    else:
        mv = int(input("Move (0-8): "))
        if 0 <= mv <= 8 and board[mv] == 0:
            board[mv] = -1
        else:
            continue
    player = -player
