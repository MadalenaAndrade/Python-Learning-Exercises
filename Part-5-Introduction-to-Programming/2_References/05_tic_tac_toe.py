# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):

    if -1 < x < 3 and -1 < y <3:
        if game_board[y][x] == "":
            game_board[y][x] = piece
            return True
    return False
            
               


if __name__=="__main__":
    game_board = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(play_turn(game_board, 2, 0, "X"))
    print(game_board)