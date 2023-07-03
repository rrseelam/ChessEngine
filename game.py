
from board import Board
from piece import Piece, Blank, Pawn, Knight, Bishop, Rook, Queen, King

game = Board()

game.print_board()

while True:

    print("input a move:")
    sr = int(input("sr = "))
    sf = int(input("sf = "))
    er = int(input("er = "))
    ef = int(input("ef = "))


    if game.move(sr, sf, er, ef):
        print("")
        game.print_board()
        print("")
    else:
        print("invalid move, try again")
