from board import Board
from heuristics import Heuristic_Model

game = Board()
HR = Heuristic_Model()
game.print_board()

while not game.is_game_over():
    print("input a move:")
    start = input("start = ")
    end = input("end = ")

    if game.move(start, end):
        print("")
        game.print_board()
        print("")
        print(HR.game_win(game))
        print(HR.diff_piece_value(game))
        print(HR.diff_area_control(game))
    else:
        print("invalid move, try again")
