import copy
def get_winner(board):
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != 0:
            return board[0][c]
    for r in range(3):
        if board[r][0] == board[r][1] == board[r][2] != 0:
            return board[r][0]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[2][0] == board[1][1] == board[0][2] != 0:
        return board[2][0]
    return 0
def minimax(board,board_empty,max = True):
    winner = get_winner(board)
    
    if winner == 1:
        return 1,None
    elif winner == 2:
        return -1,None
    if board.count(0) == 0:
        return 0,None
    
    if max:
        max_eval = -100
        best_move = None
        
        for (r,c) in board_empty:
            temp_board = copy.deepcopy(board)
            temp_board[r][c] = 1
            evalu = minimax(temp_board,False)[0]
            if evalu > max_eval:
                max_eval = evalu
                best_move = (r,c)
        return max_eval , best_move
    else:
        min_eval = 100
        best_move = None
        
        for (r,c) in board_empty:
            temp_board = copy.deepcopy(board)
            temp_board[r][c] = 1
            evalu = minimax(temp_board,True)[0]
            if evalu > min_eval:
                min_eval = evalu
                best_move = (r,c)
        return min_eval , best_move
    
