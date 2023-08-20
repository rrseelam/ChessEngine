from board import Board
from heuristics import Heuristic_Model
import copy

#takes in board state and returns the best move to make based on heuristics
#takes in the depth as to see how many move ahead to look
#need to keep track of the move and the evaluated heuristic value

#need to connect piece color to maximizing_player

class Algorithm:

    def __init__(self, depth: int) -> None:
        self.model = Heuristic_Model()
        self.depth = depth

    #returns [value, start_pos, end_pos]
    def minimax(self, state: Board, depth: int, maximizing_player: bool, player_color: str) -> list:
        #if depth reached or game is over, return the evaluation of the state
        if depth == 0 or state.is_game_over():
            return self.model.combined_hueristic_evaluation(state)
        
        if maximizing_player:
            best_move_value = -float('inf')
            best_move = ['','']
            #go through all possible moves
            pieces = state.pieces[player_color]
            for _, positions in pieces.items():
                for position in positions:
                    possible_moves = state.get_moves(position)
                    #change state, recurse
                    for move in possible_moves:
                        #does this function take in code or human?
                        end_pos = state.to_notation(move)
                        next_state = copy.deepcopy(state)
                        next_state.move(position, end_pos)
                        #see if move better than current best move
                        new_player_color = 'W' if player_color == 'B' else 'B'
                        branch_val = self.minimax(next_state, depth - 1, False, new_player_color)
                        if branch_val > best_move_value:
                            best_move_value = branch_val
                            best_move[0] = position
                            best_move[1]= end_pos

            if depth == self.depth:
                return best_move
            else:
                return best_move_value
        
        else:
            worst_move_value = float('inf')
            #go through all possible moves
            pieces = state.pieces[player_color]
            for _, positions in pieces.items():
                for position in positions:
                    possible_moves = state.get_moves(position)
                    #change state, recurse
                    for move in possible_moves:
                        #does this function take in code or human?
                        end_pos = state.to_notation(move)
                        next_state = copy.deepcopy(state)
                        next_state.move(position, end_pos)
                        #see if move better than current best move
                        new_player_color = 'W' if player_color == 'B' else 'B'
                        branch_val = self.minimax(next_state, depth - 1, False, new_player_color)
                        if branch_val < worst_move_value:
                            worst_move_value = branch_val

            return worst_move_value

    #returns [start_pos, end_pos]
    def get_move(self, state: Board, color: str) -> list:
        best_move = self.minimax(state, self.depth, True, color)
        return best_move