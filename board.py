

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

        self.white_pieces = {
            'P': ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
            'R': ['A1', 'H1'],
            'N': ['B1', 'G1'],
            'B': ['C1', 'F1'],
            'Q': ['D1'],
            'K': ['E1'],
        }

        self.white_pieces = {
            'P': ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
            'R': ['A8', 'H8'],
            'N': ['B8', 'G8'],
            'B': ['C8', 'F8'],
            'Q': ['D8'],
            'K': ['E8'],
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
        print(f"code {code}")
        res = self.locations[code[0]][code[1]]
        self.locations[code[0]][code[1]] = change
        return res

    def get_loc(self, loc) -> tuple:
        code = self.to_code(loc)
        return self.locations[code[0]][code[1]]

    def to_notation(self, loc) -> str:
        r = 0
        print(loc)
        match loc[0]:
            case 'A':
                r = 0
            case 'B':
                r = 0
            case 'C':
                r = 0
            case 'D':
                r = 0
            case 'E':
                r = 0
            case 'F':
                r = 0
            case 'G':
                r = 0
            case 'H':
                r = 0

        f = str(loc[1] + 1)  
        return (r, f)

    def to_code(self, loc) -> tuple:
        print(loc)
        r = 0
        match loc[0]:
            case 0:
                r = 'A'
            case 1:
                r = 'B'
            case 2:
                r = 'C'
            case 3:
                r = 'D'
            case 4:
                r = 'E'
            case 5:
                r = 'F'
            case 6:
                r = 'G'
            case 7:
                r = 'H'

        f = int(loc[1]) - 1
        return (r, f)

    def print_board(self):

        output = ""

        output += f"  A B C D E F G  \n"
        output += f"8 {self.locations['A8']}{self.locations['B8']}{self.locations['C8']}{self.locations['D8']}{self.locations['E8']}{self.locations['F8']}{self.locations['G8']}{self.locations['H8']} 8\n"
        output += f"7 {self.locations['A7']}{self.locations['B7']}{self.locations['C7']}{self.locations['D7']}{self.locations['E7']}{self.locations['F7']}{self.locations['G7']}{self.locations['H7']} 7\n"
        output += f"6 {self.locations['A6']}{self.locations['B6']}{self.locations['C6']}{self.locations['D6']}{self.locations['E6']}{self.locations['F6']}{self.locations['G6']}{self.locations['H6']} 6\n"
        output += f"5 {self.locations['A5']}{self.locations['B5']}{self.locations['C5']}{self.locations['D5']}{self.locations['E5']}{self.locations['F5']}{self.locations['G5']}{self.locations['H5']} 5\n"
        output += f"4 {self.locations['A4']}{self.locations['B4']}{self.locations['C4']}{self.locations['D4']}{self.locations['E4']}{self.locations['F4']}{self.locations['G4']}{self.locations['H4']} 4\n"
        output += f"3 {self.locations['A3']}{self.locations['B3']}{self.locations['C3']}{self.locations['D3']}{self.locations['E3']}{self.locations['F3']}{self.locations['G3']}{self.locations['H3']} 3\n"
        output += f"2 {self.locations['A2']}{self.locations['B2']}{self.locations['C2']}{self.locations['D2']}{self.locations['E2']}{self.locations['F2']}{self.locations['G2']}{self.locations['H2']} 2\n"
        output += f"1 {self.locations['A1']}{self.locations['B1']}{self.locations['C1']}{self.locations['D1']}{self.locations['E1']}{self.locations['F1']}{self.locations['G1']}{self.locations['H1']} 2\n"
        output += f"  A B C D E F G  \n"

        print(output)

    def check_discrete_moves(self, pos, color):

        res = []

        for (rank, file) in pos:
            if not self.validposition((rank, file)):
                continue
            if self.board[rank][file][0] != ' ' and self.board[rank][file][1] == color:
                continue
            res.append((rank, file))

        return res

    def check_diagonal_moves(self, r, f, color):

        res = []

        # up-right diagonal
        up = 1
        right = 1
        while (self.validposition((r + right, f + up))):

            if self.board[r + up][f + right][0] == ' ':
                res.append((r + up, f + right))
                up += 1
                right += 1
                continue

            if self.board[r + up][f + right][1] != color:
                res.append((r + up, f + right))

            break

        # up-left diagonal
        up = 1
        left = -1
        while (self.validposition((r + left, f + up))):

            if self.board[r + up][f + left][0] == ' ':
                res.append((r + up, f + left))
                up += 1
                left -= 1
                continue

            if self.board[r + up][f + left][1] != color:
                res.append((r + up, f + left))

            break

        # down-right diagonal
        down = -1
        right = 1
        while (self.validposition((r + right, f + down))):

            if self.board[r + down][f + right][0] == ' ':
                res.append((r + down, f + right))
                down -= 1
                right += 1
                continue

            if self.board[r + down][f + right][1] != color:
                res.append((r + down, f + right))

            break

        # down-left diagonal
        down = -1
        left = -1
        while (self.validposition((r + left, f + down))):

            if self.board[r + down][f + left][0] == ' ':
                res.append((r + down, f + left))
                down -= 1
                left -= 1
                continue

            if self.board[r + down][f + left][1] != color:
                res.append((r + down, f + left))

            break

        return res

    def check_straight_moves(self, r, f, color):

        res = []
        
        # looking right
        right = 1
        while (self.validposition(r + right, f)):

            if self.board[r + right][f][0] == ' ':
                res.append((r + right, f))
                right += 1
                continue

            if self.board[r + right][f][1] != color:
                res.append((r + right, f))

            break

        # looking left
        left = -1
        while (self.validposition(r + left, f)):

            if self.board[r + left][f][0] == ' ':
                res.append((r + left, f))
                left -= 1
                continue

            if self.board[r + left][f][1] != color:
                res.append((r + left, f))

            break

        # looking up
        up = 1
        while (self.validposition(r, f + up)):

            if self.board[r][f + up][0] == ' ':
                res.append((r, f + up))
                up += 1
                continue

            if self.board[r][f + up][1] != color:
                res.append((r, f + up))

            break

        # looking down
        down = -1
        while (self.validposition(r, f + down)):

            if self.board[r][f + down][0] == ' ':
                res.append((r, f + down))
                down -= 1
                continue

            if self.board[r][f + down][1] != color:
                res.append((r, f + down))

            break


        return res

    def get_moves(self, loc) -> list:

        piece = self.get_loc(loc)
        id = piece[0]
        color = piece[1]

        code = self.to_code(loc)
        r = code[0]
        f = code[1]

        moves = []

        match id:
            case ' ':
                pass
            case 'P':
                pass
            case 'R':
                moves += self.check_straight_moves(r, f, color)

            case 'N':

                pos = [(r + 2, f + 1), (r + 2, f - 1),
                       (r - 2, f + 1), (r - 2, f - 2),
                       (r + 1, f + 2), (r + 1, f - 2),
                       (r - 1, f + 2), (r - 1, f - 2)]

                moves += self.check_discrete_moves(pos, color)

            case 'B':
                moves += self.check_diagonal_moves(r, f, color)

            case 'Q':
                moves += self.check_diagonal_moves(r, f, color)
                moves += self.check_straight_moves(r, f, color)

            case 'K':

                pos = [(r + 1, f - 1), (r + 1, f), (r + 1, f + 1),
                       (r, f - 1),                  (r, f + 1),
                       (r - 1, f - 1), (r - 1, f), (r - 1, f + 1)]

                moves += self.check_discrete_moves(pos, color)

        return moves

    def move(self, start_loc, end_loc) -> bool:
        moves = self.get_moves(start_loc)

        piece = self.get_loc(start_loc)
        id = piece[0]
        color = piece[1]

        moves = []

        if color != self.turn:
            return False

        if end_loc not in moves:
            return False

        self.set_loc(end_loc, piece)
        self.set_loc(start_loc, (' ', ' '))
        self.toggle_turn()

        return True

    def validposition(self, code_loc) -> bool:
        r = code_loc[0]
        f = code_loc[1]
        return r >= 0 and r <= 7 and f >= 0 and f <= 7

    def toggle_turn(self):
        if self.turn == 'W':
            self.turn = 'B'
        else:
            self.turn = 'W'


if __name__ == '__main__':
    sample = Board()
    sample.print_board()
    # print("Rook",   sample.get_moves(0, 0))
    # print("Knight", sample.get_moves(0, 1))
    # print("Bishop", sample.get_moves(0, 2))
    # print("Queen",  sample.get_moves(0, 3))
    # print("King",   sample.get_moves(0, 4))
    # print("Pawn",   sample.get_moves(1, 1))

    # print("")
    # sample.move(1, 1, 3, 1)
    # sample.move(0, 1, 2, 2)

    # sample.print_board()

    # print("Pawn",   sample.get_moves(1, 1))
