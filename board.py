

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

        self.pieces = {
            'W': {
                    'P': ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
                    'R': ['A1', 'H1'],
                    'N': ['B1', 'G1'],
                    'B': ['C1', 'F1'],
                    'Q': ['D1'],
                    'K': ['E1'],
                 },

            'B': {
                    'P': ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
                    'R': ['A8', 'H8'],
                    'N': ['B8', 'G8'],
                    'B': ['C8', 'F8'],
                    'Q': ['D8'],
                    'K': ['E8'],
                 }
        }
               
        self.set_loc('A1', ('R', 'W'))
        self.set_loc('B1', ('N', 'W'))
        self.set_loc('C1', ('B', 'W'))
        self.set_loc('D1', ('Q', 'W'))
        self.set_loc('E1', ('K', 'W'))
        self.set_loc('F1', ('B', 'W'))
        self.set_loc('G1', ('N', 'W'))
        self.set_loc('H1', ('R', 'W'))

        self.set_loc('A2', ('P', 'W'))
        self.set_loc('B2', ('P', 'W'))
        self.set_loc('C2', ('P', 'W'))
        self.set_loc('D2', ('P', 'W'))
        self.set_loc('E2', ('P', 'W'))
        self.set_loc('F2', ('P', 'W'))
        self.set_loc('G2', ('P', 'W'))
        self.set_loc('H2', ('P', 'W'))

        self.set_loc('A3', (' ', ' '))
        self.set_loc('B3', (' ', ' '))
        self.set_loc('C3', (' ', ' '))
        self.set_loc('D3', (' ', ' '))
        self.set_loc('E3', (' ', ' '))
        self.set_loc('F3', (' ', ' '))
        self.set_loc('G3', (' ', ' '))
        self.set_loc('H3', (' ', ' '))

        self.set_loc('A4', (' ', ' '))
        self.set_loc('B4', (' ', ' '))
        self.set_loc('C4', (' ', ' '))
        self.set_loc('D4', (' ', ' '))
        self.set_loc('E4', (' ', ' '))
        self.set_loc('F4', (' ', ' '))
        self.set_loc('G4', (' ', ' '))
        self.set_loc('H4', (' ', ' '))

        self.set_loc('A5', (' ', ' '))
        self.set_loc('B5', (' ', ' '))
        self.set_loc('C5', (' ', ' '))
        self.set_loc('D5', (' ', ' '))
        self.set_loc('E5', (' ', ' '))
        self.set_loc('F5', (' ', ' '))
        self.set_loc('G5', (' ', ' '))
        self.set_loc('H5', (' ', ' '))

        self.set_loc('A6', (' ', ' '))
        self.set_loc('B6', (' ', ' '))
        self.set_loc('C6', (' ', ' '))
        self.set_loc('D6', (' ', ' '))
        self.set_loc('E6', (' ', ' '))
        self.set_loc('F6', (' ', ' '))
        self.set_loc('G6', (' ', ' '))
        self.set_loc('H6', (' ', ' '))

        self.set_loc('A7', ('P', 'B'))
        self.set_loc('B7', ('P', 'B'))
        self.set_loc('C7', ('P', 'B'))
        self.set_loc('D7', ('P', 'B'))
        self.set_loc('E7', ('P', 'B'))
        self.set_loc('F7', ('P', 'B'))
        self.set_loc('G7', ('P', 'B'))
        self.set_loc('H7', ('P', 'B'))

        self.set_loc('A8', ('R', 'B'))
        self.set_loc('B8', ('N', 'B'))
        self.set_loc('C8', ('B', 'B'))
        self.set_loc('D8', ('Q', 'B'))
        self.set_loc('E8', ('K', 'B'))
        self.set_loc('F8', ('B', 'B'))
        self.set_loc('G8', ('N', 'B'))
        self.set_loc('H8', ('R', 'B'))

    def set_loc(self, loc, change) -> tuple:
        code = self.to_code(loc)
        res = self.locations[code[0]][code[1]]
        self.locations[code[0]][code[1]] = change
        return res

    def get_loc(self, loc:tuple) -> tuple:
        code = loc
        return self.locations[code[0]][code[1]]
    
    def get_loc(self, loc:str) -> tuple:
        code = self.to_code(loc)
        return self.locations[code[0]][code[1]]

    def to_notation(self, loc) -> str:
        r = 'T'
        
        if loc[0] == 0:
            r = 'A'
        elif loc[0] == 1:
            r = 'B'
        elif loc[0] == 2:
            r = 'C'
        elif loc[0] == 3:
            r = 'D'
        elif loc[0] == 4:
            r = 'E'
        elif loc[0] == 5:
            r = 'F'
        elif loc[0] == 6:
            r = 'G'
        elif loc[0] == 7:
            r = 'H'


        f = str(loc[1] + 1)  
        return r + f

    def to_code(self, loc) -> tuple:

        r = 0
        
        if loc[0] == 'A':
                r = 0
        elif loc[0] == 'B':
                r = 1
        elif loc[0] == 'C':
            r = 2
        elif loc[0] == 'D':
                r = 3
        elif loc[0] == 'E':
            r = 4
        elif loc[0] == 'F':
            r = 5
        elif loc[0] == 'G':
            r = 6
        elif loc[0] == 'H':
            r = 7

        f = int(loc[1]) - 1
        return (r, f)

    def print_board(self):

        output = ""

        output += f"  ABCDEFGH \n"
        output += f"8 {self.get_loc('A8')[0]}{self.get_loc('B8')[0]}{self.get_loc('C8')[0]}{self.get_loc('D8')[0]}{self.get_loc('E8')[0]}{self.get_loc('F8')[0]}{self.get_loc('G8')[0]}{self.get_loc('H8')[0]} 8\n"
        output += f"7 {self.get_loc('A7')[0]}{self.get_loc('B7')[0]}{self.get_loc('C7')[0]}{self.get_loc('D7')[0]}{self.get_loc('E7')[0]}{self.get_loc('F7')[0]}{self.get_loc('G7')[0]}{self.get_loc('H7')[0]} 7\n"
        output += f"6 {self.get_loc('A6')[0]}{self.get_loc('B6')[0]}{self.get_loc('C6')[0]}{self.get_loc('D6')[0]}{self.get_loc('E6')[0]}{self.get_loc('F6')[0]}{self.get_loc('G6')[0]}{self.get_loc('H6')[0]} 6\n"
        output += f"5 {self.get_loc('A5')[0]}{self.get_loc('B5')[0]}{self.get_loc('C5')[0]}{self.get_loc('D5')[0]}{self.get_loc('E5')[0]}{self.get_loc('F5')[0]}{self.get_loc('G5')[0]}{self.get_loc('H5')[0]} 5\n"
        output += f"4 {self.get_loc('A4')[0]}{self.get_loc('B4')[0]}{self.get_loc('C4')[0]}{self.get_loc('D4')[0]}{self.get_loc('E4')[0]}{self.get_loc('F4')[0]}{self.get_loc('G4')[0]}{self.get_loc('H4')[0]} 4\n"
        output += f"3 {self.get_loc('A3')[0]}{self.get_loc('B3')[0]}{self.get_loc('C3')[0]}{self.get_loc('D3')[0]}{self.get_loc('E3')[0]}{self.get_loc('F3')[0]}{self.get_loc('G3')[0]}{self.get_loc('H3')[0]} 3\n"
        output += f"2 {self.get_loc('A2')[0]}{self.get_loc('B2')[0]}{self.get_loc('C2')[0]}{self.get_loc('D2')[0]}{self.get_loc('E2')[0]}{self.get_loc('F2')[0]}{self.get_loc('G2')[0]}{self.get_loc('H2')[0]} 2\n"
        output += f"1 {self.get_loc('A1')[0]}{self.get_loc('B1')[0]}{self.get_loc('C1')[0]}{self.get_loc('D1')[0]}{self.get_loc('E1')[0]}{self.get_loc('F1')[0]}{self.get_loc('G1')[0]}{self.get_loc('H1')[0]} 1\n"
        output += f"  ABCDEFGH \n"

        print(output)

    def check_discrete_moves(self, pos, color):

        res = []

        for (rank, file) in pos:
            if not self.validposition((rank, file)):
                continue
            if self.locations[rank][file][0] != ' ' and self.locations[rank][file][1] == color:
                continue
            res.append((rank, file))

        return res

    def check_pawn_moves(self, r, f, color):
        dir = 0
        not_moved = False
        if color == 'W':
            dir = 1
            not_moved = f == 1
        else:
            dir = -1
            not_moved = f == 6
        
        moves = []
        # currently cannot handle changing to queen at the end of the board
   
        if self.validposition((r, f + dir)) and self.locations[r][f + dir][0] == ' ':
            moves.append((r, f + dir))

            if not_moved and self.validposition((r, f + dir + dir)) and self.locations[r][f + dir + dir][0] == ' ':
                moves.append((r, f + dir + dir))

        if self.validposition((r + 1, f + dir)) and self.locations[r + 1][f + dir][0] != ' ' and self.locations[r + 1][f + dir][1] != color:
            moves.append((r + 1, f + dir))

        if self.validposition((r - 1, f + dir)) and self.locations[r - 1][f + dir][0] != ' ' and self.locations[r - 1][f + dir][1] != color:
            moves.append((r - 1, f + dir))

        return moves

    def check_diagonal_moves(self, r, f, color):

        res = []

        # up-right diagonal
        up = 1
        right = 1
        while (self.validposition((r + right, f + up))):

            if self.locations[r+right][f+up] == ' ':
                res.append((r + right, f + up))
                up += 1
                right += 1
                continue

            if self.locations[r + right][f + up][1] != color:
                res.append((r + right, f + up))

            break

        # up-left diagonal
        up = 1
        left = -1
        while (self.validposition((r + left, f + up))):

            if self.locations[r + left][f + up][0] == ' ':
                res.append((r + left, f + up))
                up += 1
                left -= 1
                continue

            if self.locations[r + left][f + up][1] != color:
                res.append((r + left, f + up))

            break

        # down-right diagonal
        down = -1
        right = 1
        while (self.validposition((r + right, f + down))):

            if self.locations[r + right][f + down][0] == ' ':
                res.append((r + right, f + down))
                down -= 1
                right += 1
                continue

            if self.locations[r + right][f + down][1] != color:
                res.append((r + right, f + down))

            break

        # down-left diagonal
        down = -1
        left = -1
        while (self.validposition((r + left, f + down))):

            if self.locations[r + left][f + down][0] == ' ':
                res.append((r + left, f + down))
                down -= 1
                left -= 1
                continue

            if self.locations[r + left][f + down][1] != color:
                res.append((r + left, f + down))

            break

        return res

    def check_straight_moves(self, r, f, color):

        res = []
        
        # looking right
        right = 1
        while (self.validposition((r + right, f))):

            if self.locations[r + right][f][0] == ' ':
                res.append((r + right, f))
                right += 1
                continue

            if self.locations[r + right][f][1] != color:
                res.append((r + right, f))

            break

        # looking left
        left = -1
        while (self.validposition((r + left, f))):

            if self.locations[r + left][f][0] == ' ':
                res.append((r + left, f))
                left -= 1
                continue

            if self.locations[r + left][f][1] != color:
                res.append((r + left, f))

            break

        # looking up
        up = 1
        while (self.validposition((r, f + up))):

            if self.locations[r][f + up][0] == ' ':
                res.append((r, f + up))
                up += 1
                continue

            if self.locations[r][f + up][1] != color:
                res.append((r, f + up))

            break

        # looking down
        down = -1
        while (self.validposition((r, f + down))):

            if self.locations[r][f + down][0] == ' ':
                res.append((r, f + down))
                down -= 1
                continue

            if self.locations[r][f + down][1] != color:
                res.append((r, f + down))

            break


        return res
    
    def print_moves(self, loc):
        moves = self.get_moves(loc)
        output = []

        for move in moves:
            output.append(self.to_notation(move))
        return output

    def get_moves(self, loc) -> list:

        piece = self.get_loc(loc)
        id = piece[0]
        color = piece[1]

        code = self.to_code(loc)
        r = code[0]
        f = code[1]

        moves = []

        if id == ' ':
            pass
        elif id == 'P':
            moves = self.check_pawn_moves(r, f, color)
        elif id == 'R':
            moves += self.check_straight_moves(r, f, color)

        elif id == 'N':

            pos = [(r + 2, f + 1), (r + 2, f - 1),
                    (r - 2, f + 1), (r - 2, f - 2),
                    (r + 1, f + 2), (r + 1, f - 2),
                    (r - 1, f + 2), (r - 1, f - 2)]

            moves += self.check_discrete_moves(pos, color)

        elif id == 'B':
            moves += self.check_diagonal_moves(r, f, color)

        elif id == 'Q':
            moves += self.check_diagonal_moves(r, f, color)
            moves += self.check_straight_moves(r, f, color)

        elif id == 'K':

            pos = [(r + 1, f - 1), (r + 1, f), (r + 1, f + 1),
                    (r, f - 1),                  (r, f + 1),
                    (r - 1, f - 1), (r - 1, f), (r - 1, f + 1)]

            moves += self.check_discrete_moves(pos, color)

        return moves
    
    def in_check(self, color):
        state = self.locations
        king_loc = self.locations[color]['K']
        king_loc_code = self.to_code(king_loc)
        
        rank = king_loc_code[0]
        file = king_loc_code[1]

        possible_positions = {
            'P': [(1,-1), (1,1)],
            'N': [(2, 1), (2,-1),(-2, 1), (-2, -2),
                  (1, 2), (1, -2), (-1, 2), (1, -2)],
        }

        #checks pawn and knight positions
        for key, value in possible_positions.items():
            for pos in value:
                checkrank, checkfile = rank + pos[0], file + pos[1]
                if self.validposition((checkrank, checkfile)) and state[checkrank][checkfile][0] == key:
                    if state[checkrank][checkfile][1] != color:
                        return True
                
    
        #check rook, bishop, and queen positions
        #rook + queen checks    
        #check upwards
        up = file + 1
        while up <= 7:
            current_piece = state[rank][up]
            if current_piece[0] == '.':
                up += 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'R' or current_piece[0] == 'Q':
                        return True
                break

        #check downwards
        down = file - 1
        while down >= 0:
            current_piece = state[rank][down]
            if current_piece[0] == '.':
                down -= 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'R' or current_piece[0] == 'Q':
                        return True
                break
    
        #check right
        right = rank + 1
        while right <= 7:
            current_piece = state[right][file]
            if current_piece[0] == '.':
                right += 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'R' or current_piece[0] == 'Q':
                        return True
                break
    
        #check left
        left = rank - 1
        while left >= 0:
            current_piece = state[left][file]
            if current_piece[0] == '.':
                left -= 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'R' or current_piece[0] == 'Q':
                        return True
                break

        #bishop + queen checks
        # up-right diagonal
        right = 1
        up = 1
        while (self.validposition((rank + right, file + up))):
            current_piece = state[rank + right][file + up]
            if current_piece[0] == '.':
                right += 1
                up += 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'B' or current_piece[0] == 'Q':
                        return True
                break            

        # up-left diagonal
        left = -1
        up = 1
        while (self.validposition((rank + left, file + up))):
            current_piece = state[rank + left][file + up]
            if current_piece[0] == '.':
                left -= 1
                up += 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'B' or current_piece[0] == 'Q':
                        return True
                break
    
        # down-right diagonal
        right = 1
        down = -1
        while (self.validposition((rank + right, file + down))):
            current_piece = state[rank + right][file + down]
            if current_piece[0] == '.':
                right += 1
                down -= 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'B' or current_piece[0] == 'Q':
                        return True
                break            

        # down-left diagonal
        left = -1
        down = -1
        while (self.validposition((rank + left, file + down))):
            current_piece = state[rank + left][file + down]
            if current_piece[0] == '.':
                left -= 1
                down -= 1
            else:
                if current_piece[1] != color:
                    if current_piece[0] == 'B' or current_piece[0] == 'Q':
                        return True
                break  

        return False


    def move(self, start_loc, end_loc) -> bool:

        moves = self.get_moves(start_loc)
        piece = self.get_loc(start_loc)

        p_id = piece[0]
        p_color = piece[1]

        target = self.get_loc(end_loc)
        t_id = target[0]
        t_color = target[1]

        if p_color != self.turn:
            return False

        if self.to_code(end_loc) not in moves:
            return False
        
        self.set_loc(end_loc, piece)
        self.set_loc(start_loc, (' ', ' '))
        self.toggle_turn()

        self.pieces[p_color][p_id].remove(start_loc)
        self.pieces[p_color][p_id].append(end_loc)
        
        if t_id != ' ':
            self.pieces[t_color][t_id].remove(end_loc)

        if end_loc[1] == 7 and p_id == 'P':
            self.set_loc((end_loc) , ('Q', p_color))
            self.pieces[p_color]['Q'].append(self.to_notation(end_loc))
            self.pieces[p_color]['P'].remove(self.to_notation(end_loc))
            
        return True

    def validposition(self, code_loc:tuple) -> bool:
        r = code_loc[0]
        f = code_loc[1]
        return r >= 0 and r <= 7 and f >= 0 and f <= 7
    
    def toggle_turn(self):
        if self.turn == 'W':
            self.turn = 'B'
        else:
            self.turn = 'W'

    def is_game_over(self):
        if len(self.pieces['W']['K']) == 0:
            return True
        if len(self.pieces['B']['K']) == 0:
            return True
        return False
    
    def winner(self):
        if len(self.pieces['W']['K']) == 0:
            return 'W'
        return 'B'

if __name__ == '__main__':
    sample = Board()
    sample.print_board()
    print("Rook",   sample.print_moves('A1'))
    print("Knight", sample.print_moves('B1'))
    print("Bishop", sample.print_moves('C1'))
    print("Queen",  sample.print_moves('D1'))
    print("King",   sample.print_moves('E1'))
    print("Pawn",   sample.print_moves('E2'))
    sample.move('B1', 'C3')
    sample.print_board()
    print("Knight", sample.print_moves('C3'))
    print("Rook",   sample.print_moves('A1'))
    print("Knight", sample.print_moves('B1'))
    print("Bishop", sample.print_moves('C1'))
    print("Queen",  sample.print_moves('D1'))
    print("Pawn",   sample.print_moves('E2'))
    print("Pawn",   sample.print_moves('E7'))
    sample.move('E7', 'E5')
    sample.print_board()
    print("Pawn",   sample.print_moves('E5'))
    

    print(sample.pieces)

    # print("")
    # sample.move(1, 1, 3, 1)
    # sample.move(0, 1, 2, 2)

    # sample.print_board()

    # print("Pawn",   sample.get_moves(1, 1))
