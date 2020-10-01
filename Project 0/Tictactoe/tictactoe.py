"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # initializing count to determine who has the next turn (determine by no. of X or O)
    x_count = 0
    o_count = 0
    for i in range(0, 3):
        for j in range(0, 3):  # nested loop :)
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1

    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_action = set()  # requirement to return (i, j) in a set

    for i in range(0, 3):
        for j in range(0, 3):
            # an EMPTY slot signifies a possible action user/ai can take
            if board[i][j] == EMPTY:
                possible_action.add((i, j))

    return possible_action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = deepcopy(board)

    if new_board[action[0]][action[1]] != EMPTY:
        raise Exception("action must be EMPTY")
    else:
        new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    """
    If it is horizontal win example:
        [X,X,X]
        [O, ,O]
        [O, , ]
    
    If it is vertical win, example:
        [X,O, ]
        [X,X,O]
        [X,O,O]
    """
    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:  # horizontal win
            return board[i][0]
        if board[0][i] != EMPTY and board[0][i] == board[1][i] and board[1][i] == board[2][i]:  # vertical win
            return board[0][i]  # checks for both X and O
    """
    If it is downwards diagonal win, example:
        [X, , ]
        [ ,X, ]
        [ , ,X]
    """
    if board[0][0] != EMPTY and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]
    """
        If it is upwards diagonal win, example:
            [ , ,X]
            [ ,X, ]
            [X, , ]
    """
    if board[0][2] != EMPTY and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(0, 3):
            for j in range(0, 3):
                if board[i][j] == EMPTY:
                    return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Player X is max while Player O is mini
    if terminal(board):
        return None

    if player(board) == X:  # objective is to maximise value
        value = -math.inf  # worst-case scenario for AI
        best_move = None

        for action in actions(board):
            minimum_value = min_value(result(board, action))

            if minimum_value > value:
                value = minimum_value
                best_move = action

    elif player(board) == O:  # objective is to minimise value
        value = math.inf  # worst-case scenario for AI
        best_move = None

        for action in actions(board):
            maximum_value = max_value(result(board, action))
            if maximum_value < value:
                value = maximum_value
                best_move = action

    return best_move


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v


def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v
