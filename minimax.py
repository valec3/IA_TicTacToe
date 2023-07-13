from math import inf as infinity
from board import empty_cells

def evaluate(state):
    if wins(state, 1):
        score = +1
    elif wins(state, -1):
        score = -1
    else:
        score = 0
    return score

def wins(state, player):

    win_state = [
        [state[0][0], state[0][1], state[0][2]],
        [state[1][0], state[1][1], state[1][2]],
        [state[2][0], state[2][1], state[2][2]],
        [state[0][0], state[1][0], state[2][0]],
        [state[0][1], state[1][1], state[2][1]],
        [state[0][2], state[1][2], state[2][2]],
        [state[0][0], state[1][1], state[2][2]],
        [state[2][0], state[1][1], state[0][2]],
    ]
    return [player, player, player] in win_state


def minimax(state, depth, player):
	if player == +1:
		best_move = [-1, -1, -infinity]
	else:
		best_move = [-1, -1, +infinity]

	if depth == 0 or (wins(state, -1) or wins(state, +1)):
		score = evaluate(state)
		return [-1, -1, score]

	for cell in empty_cells(state):
		x, y = cell[0], cell[1]
		state[x][y] = player
		score = minimax(state, depth - 1, -player)
		state[x][y] = 0
		score[0], score[1] = x, y

		if player == +1:
			if score[2] > best_move[2]:
				best_move = score
		else:
			if score[2] < best_move[2]:
				best_move = score

	return best_move