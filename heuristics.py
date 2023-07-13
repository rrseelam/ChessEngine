from board import Board

# this class is a set of fucntions that accept board positions as input, and can generates heuristics
# each heuristic will be in the form of a number. A more positive number indicates a winning position for W
# a more negative number indicates a winning position for black
# some linear or non linear combination of the heuristics can be passed into the optimization function

class Heuristic_Model:

    def __init__(self) -> None:
        pass

    def game_win(self, b: Board) -> float:
        if b.is_game_over():
            return 1 if b.winner() == 'W' else -1
        return 0
    
    def diff_piece_value(self, b: Board) -> float:
        diff = 0

        diff += len(b.pieces['W']['P']) * 1
        diff -= len(b.pieces['B']['P']) * 1

        diff += len(b.pieces['W']['N']) * 6.2
        diff -= len(b.pieces['B']['N']) * 6.2

        diff += len(b.pieces['W']['B']) * 6.55
        diff -= len(b.pieces['B']['B']) * 6.55

        diff += len(b.pieces['W']['R']) * 10.31
        diff -= len(b.pieces['B']['R']) * 10.31

        diff += len(b.pieces['W']['Q']) * 20.14
        diff -= len(b.pieces['B']['Q']) * 20.14

        return diff
    
    def diff_area_control(self, b: Board) -> float:
        diff = 0

        for i in range(0, 8):
            for j in range(0, 8):
                loc = b.to_notation((i, j))
                if b.get_loc(loc)[1] == 'W':
                    diff += len(b.get_moves(loc))

                if b.get_loc(loc)[1] == 'B':
                    diff -= len(b.get_moves(loc))
                    
        return diff