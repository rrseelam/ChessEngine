import numpy as np
from piece import Piece, Blank, Pawn, Knight, Bishop, Rook, Queen, King

class Board:

    def __init__(self):

        self.turn = 'W'
        self.locations = [[None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None],
                          [None, None, None, None, None, None, None, None]]
        
        self.white_pieces = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                             (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),]
        self.black_pieces = [(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                             (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),]
        
        self.locations[0][0] = Rook    (0, 0, 'W', self)
        self.locations[0][1] = Knight  (0, 1, 'W', self)
        self.locations[0][2] = Bishop  (0, 2, 'W', self)
        self.locations[0][3] = Queen   (0, 3, 'W', self)
        self.locations[0][4] = King    (0, 4, 'W', self)
        self.locations[0][5] = Bishop  (0, 5, 'W', self)
        self.locations[0][6] = Knight  (0, 6, 'W', self)
        self.locations[0][7] = Rook    (0, 7, 'W', self)

        self.locations[1][0] = Pawn    (1, 0, 'W', self)
        self.locations[1][1] = Pawn    (1, 1, 'W', self)
        self.locations[1][2] = Pawn    (1, 2, 'W', self)
        self.locations[1][3] = Pawn    (1, 3, 'W', self)
        self.locations[1][4] = Pawn    (1, 4, 'W', self)
        self.locations[1][5] = Pawn    (1, 5, 'W', self)
        self.locations[1][6] = Pawn    (1, 6, 'W', self)
        self.locations[1][7] = Pawn    (1, 7, 'W', self)

        self.locations[2][0] = Blank   (2, 0, 'W', self)
        self.locations[2][1] = Blank   (2, 1, 'W', self)
        self.locations[2][2] = Blank   (2, 2, 'W', self)
        self.locations[2][3] = Blank   (2, 3, 'W', self)
        self.locations[2][4] = Blank   (2, 4, 'W', self)
        self.locations[2][5] = Blank   (2, 5, 'W', self)
        self.locations[2][6] = Blank   (2, 6, 'W', self)
        self.locations[2][7] = Blank   (2, 7, 'W', self)

        self.locations[3][0] = Blank   (3, 0, 'W', self)
        self.locations[3][1] = Blank   (3, 1, 'W', self)
        self.locations[3][2] = Blank   (3, 2, 'W', self)
        self.locations[3][3] = Blank   (3, 3, 'W', self)
        self.locations[3][4] = Blank   (3, 4, 'W', self)
        self.locations[3][5] = Blank   (3, 5, 'W', self)
        self.locations[3][6] = Blank   (3, 6, 'W', self)
        self.locations[3][7] = Blank   (3, 7, 'W', self)

        self.locations[4][0] = Blank   (4, 0, 'W', self)
        self.locations[4][1] = Blank   (4, 1, 'W', self)
        self.locations[4][2] = Blank   (4, 2, 'W', self)
        self.locations[4][3] = Blank   (4, 3, 'W', self)
        self.locations[4][4] = Blank   (4, 4, 'W', self)
        self.locations[4][5] = Blank   (4, 5, 'W', self)
        self.locations[4][6] = Blank   (4, 6, 'W', self)
        self.locations[4][7] = Blank   (4, 7, 'W', self)

        self.locations[5][0] = Blank   (5, 0, 'W', self)
        self.locations[5][1] = Blank   (5, 1, 'W', self)
        self.locations[5][2] = Blank   (5, 2, 'W', self)
        self.locations[5][3] = Blank   (5, 3, 'W', self)
        self.locations[5][4] = Blank   (5, 4, 'W', self)
        self.locations[5][5] = Blank   (5, 5, 'W', self)
        self.locations[5][6] = Blank   (5, 6, 'W', self)
        self.locations[5][7] = Blank   (5, 7, 'W', self)

        self.locations[6][0] = Pawn    (6, 0, 'B', self)
        self.locations[6][1] = Pawn    (6, 1, 'B', self)
        self.locations[6][2] = Pawn    (6, 2, 'B', self)
        self.locations[6][3] = Pawn    (6, 3, 'B', self)
        self.locations[6][4] = Pawn    (6, 4, 'B', self)
        self.locations[6][5] = Pawn    (6, 5, 'B', self)
        self.locations[6][6] = Pawn    (6, 6, 'B', self)
        self.locations[6][7] = Pawn    (6, 7, 'B', self)

        self.locations[7][0] = Rook    (7, 0, 'B', self)
        self.locations[7][1] = Knight  (7, 1, 'B', self)
        self.locations[7][2] = Bishop  (7, 2, 'B', self)
        self.locations[7][3] = King    (7, 3, 'B', self)
        self.locations[7][4] = Queen   (7, 4, 'B', self)
        self.locations[7][5] = Bishop  (7, 5, 'B', self)
        self.locations[7][6] = Knight  (7, 6, 'B', self)
        self.locations[7][7] = Rook    (7, 7, 'B', self)

    def get_board_state(self):
        return self.locations

    def print_board(self):
        output = ""
        for i in range(8):
            for j in range(8):
                output += self.locations[i][j].get_id()
            output += '\n'
        print(output)

    def get_moves(self, rank, file):
       return self.locations[rank][file].get_moves()
    
    def move(self, sr, sf, er, ef):
        self.locations[er][ef] = self.locations[sr][sf]
        self.locations[er][ef].move_piece(er, ef)
        self.locations[sr][sf] = Blank(sr, sf, 'W', self)


    def toggle_turn(self):
        if self.turn == 'W':
            self.turn = 'B'
        else:
            self.turn = 'W'

    def toggle_turn(self):
        if self.turn == 'W':
            self.turn = 'B'
        else:
            self.turn = 'W'

if __name__ == '__main__':
    sample = Board()
    sample.print_board()
    print("Rook",   sample.get_moves(0, 0))
    print("Knight", sample.get_moves(0, 1))
    print("Bishop", sample.get_moves(0, 2))
    print("Queen",  sample.get_moves(0, 3))
    print("King",   sample.get_moves(0, 4))
    print("Pawn",   sample.get_moves(1, 1))

