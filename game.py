
from board import Board
from heuristics import Heuristic_Model

game = Board()

game.print_board()

HR = Heuristic_Model()

print(HR.game_win(game))
print(HR.diff_piece_value(game))
print(HR.diff_area_control(game))
# while True:

#     print("input a move:")
#     sr = int(input("sr = "))
#     sf = int(input("sf = "))
#     er = int(input("er = "))
#     ef = int(input("ef = "))

#     if game.move(sr, sf, er, ef):
#         print("")
#         game.print_board()
#         print("")
#     else:
#         print("invalid move, try again")
