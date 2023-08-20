from board import Board
from heuristics import Heuristic_Model
from algorithm import Algorithm

game = Board()
HR = Heuristic_Model()
algo = Algorithm(3)

game.print_board()

while not game.is_game_over():
    print("input a move:")
    start = input("start = ")
    end = input("end = ")

    if game.move(start, end):
        print("")
        game.print_board()
        print("")
        # print(HR.game_win(game))
        # print(HR.diff_piece_value(game))
        # print(HR.diff_area_control(game))

        algo_move = algo.get_move(game,game.turn)
        game.move(algo_move[0],algo_move[1])
        
        print("")
        game.print_board()
        print("")
    else:
        print("invalid move, try again")
