def play_turn(game_board: list, x: int, y: int, piece: str):
    if x in [0,1,2] and y in [0,1,2] and game_board[y][x] == "" and piece in ['X', 'O']:
        game_board[y][x] = piece
        return True
    else:
        return False

'''
def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 0 or y < 0 or x > 2 or y > 2:
        return False
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False
This might be slightly more readable to a human, but I'm not sure I'd split the testing up.
I've always been taught to combine lines unless it makes it completely incomprehensible to humans.
'''