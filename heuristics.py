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
    
    def diff_pawn_development(self, b: Board) -> int:
        diff = 0
        
        for white_pawn in b.pieces['W']['P']:
            pawn_pos = b.to_code(white_pawn)
            diff += pawn_pos[1] - 1
            
        for black_pawn in b.pieces['B']['P']:
            pawn_pos = b.to_code(black_pawn)
            diff -= abs(pawn_pos[1] - 6)
            
        return diff
    
    def diff_overall_development(self, b: Board) -> int:
        diff = 0
        
        for piece, positions in b.pieces['W'].items():
            for position in positions:
                curr_position = b.to_code(position)
                if piece == 'P':
                    diff += curr_position[1] - 1
                else:
                    diff += curr_position[1] - 0
            
            
        for piece, positions in b.pieces['B'].items():
            for position in positions:
                curr_position = b.to_code(position)
                if piece == 'P':
                    diff -= abs(curr_position[1] - 6)
                else:
                    diff -= abs(curr_position[1] - 7)
                    
        return diff
    
    #need to scale individual heuristics to 0-1
    def combined_hueristic_evaluation(self, b: Board) -> float:
        if self.game_win(b) != 0:
            return self.game_win(b) * float('inf')
        else:
            total = 0
            total += self.diff_area_control(b)
            total += self.diff_overall_development(b)
            total += self.diff_pawn_development(b)
            total += self.diff_piece_value(b)

            return total