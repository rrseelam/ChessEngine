
class Piece:

    def __init__(self, rank, file, color, board):
        self.rank = rank      # 0 - 7
        self.file = file      # 0 - 7
        self.color = color    # 'W' or 'B'
        self.board = board

    def get_location(self):
        return (self.rank, self.file)

    def get_moves(self, state):
        return []

    def move_piece(self, r, f):
        self.rank = r
        self.file = f

    def get_id(self):
        return 'T'

    def get_color(self):
        return self.color


class Blank(Piece):

    def __init__(self, rank, file, color, board):
        super().__init__(rank, file, color, board)

    def get_moves(self):
        return []

    def get_id(self):
        return '.'


class Pawn(Piece):

    def __init__(self, rank, file, color, board):
        super().__init__(rank, file, color, board)
        self.first_move = True

    def get_moves(self):
        if self.color == 'W':
            return self.get_moves_white()
        return self.get_moves_black()
    
    def get_moves_white(self):
        res = []
        state = self.board.locations
        # currently cannot handle changing to queen at the end of the board
        # currently cannot move black pawns because its always + 1

        if state[self.rank + 1][self.file + 1].get_id() != '.' and state[self.rank + 1][self.file + 1].get_color() != self.color:
            res.append((self.rank + 1, self.file + 1))

        if state[self.rank + 1][self.file - 1].get_id() != '.' and state[self.rank + 1][self.file - 1].get_color() != self.color:
            res.append((self.rank + 1, self.file - 1))

        if state[self.rank + 1][self.file].get_id() == '.':
            res.append((self.rank + 1, self.file))

        if self.first_move and state[self.rank + 2][self.file].get_id() == '.':
            res.append((self.rank + 2, self.file))

        return res
    
    def get_moves_black(self):
        res = []
        state = self.board.locations
        # currently cannot handle changing to queen at the end of the board
        # currently cannot move black pawns because its always + 1

        if state[self.rank - 1][self.file + 1].get_id() != '.' and state[self.rank - 1][self.file + 1].get_color() != self.color:
            res.append((self.rank - 1, self.file + 1))

        if state[self.rank - 1][self.file - 1].get_id() != '.' and state[self.rank - 1][self.file - 1].get_color() != self.color:
            res.append((self.rank - 1, self.file - 1))

        if state[self.rank - 1][self.file].get_id() == '.':
            res.append((self.rank - 1, self.file))

        if self.first_move and state[self.rank - 2][self.file].get_id() == '.':
            res.append((self.rank - 2, self.file))

        return res

    def move_piece(self, r, f):
        self.rank = r
        self.file = f
        self.first_move = False

    def get_id(self):
        return 'P'


class Knight(Piece):

    def __init__(self, rank, file, color, board):
        super().__init__(rank, file, color, board)

    def get_moves(self):

        state = self.board.locations

        pos = [(self.rank + 2, self.file + 1), (self.rank + 2, self.file - 1),
               (self.rank - 2, self.file + 1), (self.rank - 2, self.file - 2),
               (self.rank + 1, self.file + 2), (self.rank + 1, self.file - 2),
               (self.rank - 1, self.file + 2), (self.rank - 1, self.file - 2)]

        res = []

        for (rank, file) in pos:
            if rank > 7 or rank < 0:
                continue
            if file > 7 or file < 0:
                continue
            if state[rank][file].get_id() != '.' and state[rank][file].get_color() == self.color:
                continue
            res.append((rank, file))

        return res

    def get_id(self):
        return 'N'


class Bishop(Piece):

    def __init__(self, rank, file, color, board):
        super().__init__(rank, file, color, board)

    def get_moves(self):

        res = []
        state = self.board.locations

        # up-right diagonal
        up = 1
        right = 1
        while (self.rank + up <= 7 and self.file + right <= 7):

            if state[self.rank + up][self.file + right].get_id() == '.':
                res.append((self.rank + up, self.file + right))
                up += 1
                right += 1
                continue

            if state[self.rank + up][self.file + right].get_color() != self.color:
                res.append((self.rank + up, self.file + right))

            break

        # up-left diagonal
        up = 1
        left = -1
        while (self.rank + up <= 7 and self.file + left >= 0):

            if state[self.rank + up][self.file + left].get_id() == '.':
                res.append((self.rank + up, self.file + left))
                up += 1
                left -= 1
                continue

            if state[self.rank + up][self.file + left].get_color() != self.color:
                res.append((self.rank + up, self.file + left))

            break

        # down-right diagonal
        down = -1
        right = 1
        while (self.rank + down >= 0 and self.file + right <= 7):

            if state[self.rank + down][self.file + right].get_id() == '.':
                res.append((self.rank + down, self.file + right))
                down -= 1
                right += 1
                continue

            if state[self.rank + down][self.file + right].get_color() != self.color:
                res.append((self.rank + down, self.file + right))

            break

        # down-left diagonal
        down = -1
        left = -1
        while (self.rank + down >= 0 and self.file + left >= 0):

            if state[self.rank + down][self.file + left].get_id() == '.':
                res.append((self.rank + down, self.file + left))
                down -= 1
                left -= 1
                continue

            if state[self.rank + down][self.file + left].get_color() != self.color:
                res.append((self.rank + down, self.file + left))

            break

        return res

    def get_id(self):
        return 'B'


class Rook(Piece):

    def __init__(self, rank, file, color, board):
        super().__init__(rank, file, color, board)

    def get_moves(self):

        res = []
        state = self.board.locations

        # looking right
        pos_file = self.file + 1
        while (pos_file <= 7):
            if state[self.rank][pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file += 1
            elif state[self.rank][pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank][pos_file].get_color() == self.color:
                break

        # looking left
        pos_file = self.file - 1
        while (pos_file >= 0):
            if state[self.rank][pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file -= 1
            elif state[self.rank][pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank][pos_file].get_color() == self.color:
                break

        # looking up
        pos_rank = self.rank + 1
        while (pos_rank <= 7):
            if state[pos_rank][self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank += 1
            elif state[pos_rank][self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank][self.rank].get_color() == self.color:
                break

        # looking down
        pos_rank = self.rank + 1
        while (pos_rank >= 0):
            if state[pos_rank][self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank -= 1
            elif state[pos_rank][self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank][self.rank].get_color() == self.color:
                break

        return res

    def get_id(self):
        return 'R'


class Queen(Piece):

    def __init__(self, rank, file, color, board):
        super().__init__(rank, file, color, board)

    def get_moves(self):

        state = self.board.locations
        res = []

        # up-right diagonal
        up = 1
        right = 1
        while (self.rank + up <= 7 and self.file + right <= 7):

            if state[self.rank + up][self.file + right].get_id() == '.':
                res.append((self.rank + up, self.file + right))
                up += 1
                right += 1
                continue

            if state[self.rank + up][self.file + right].get_color() != self.color:
                res.append((self.rank + up, self.file + right))

            break

        # up-left diagonal
        up = 1
        left = -1
        while (self.rank + up <= 7 and self.file + left >= 0):

            if state[self.rank + up][self.file + left].get_id() == '.':
                res.append((self.rank + up, self.file + left))
                up += 1
                left -= 1
                continue

            if state[self.rank + up][self.file + left].get_color() != self.color:
                res.append((self.rank + up, self.file + left))

            break

        # down-right diagonal
        down = -1
        right = 1
        while (self.rank + down >= 0 and self.file + right <= 7):

            if state[self.rank + down][self.file + right].get_id() == '.':
                res.append((self.rank + down, self.file + right))
                down -= 1
                right += 1
                continue

            if state[self.rank + down][self.file + right].get_color() != self.color:
                res.append((self.rank + down, self.file + right))

            break

        # down-left diagonal
        down = -1
        left = -1
        while (self.rank + down >= 0 and self.file + left >= 0):

            if state[self.rank + down][self.file + left].get_id() == '.':
                res.append((self.rank + down, self.file + left))
                down -= 1
                left -= 1
                continue

            if state[self.rank + down][self.file + left].get_color() != self.color:
                res.append((self.rank + down, self.file + left))

            break

        # looking right
        pos_file = self.file + 1
        while (pos_file <= 7):
            if state[self.rank][pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file += 1
            elif state[self.rank][pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank][pos_file].get_color() == self.color:
                break

        # looking left
        pos_file = self.file - 1
        while (pos_file >= 0):
            if state[self.rank][pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file -= 1
            elif state[self.rank][pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank][pos_file].get_color() == self.color:
                break

        # looking up
        pos_rank = self.rank + 1
        while (pos_rank <= 7):
            if state[pos_rank][self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank += 1
            elif state[pos_rank][self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank][self.rank].get_color() == self.color:
                break

        # looking down
        pos_rank = self.rank - 1
        while (pos_rank >= 0):
            if state[pos_rank][self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank -= 1
            elif state[pos_rank][self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank][self.rank].get_color() == self.color:
                break
       
        return res

    def get_id(self):
        return 'Q'


class King(Piece):

    def __init__(self, rank, file, color, board):
        super().__init__(rank, file, color, board)

    def get_moves(self):

        state = self.board.locations

        pos = [(self.rank + 1, self.file - 1), (self.rank + 1, self.file), (self.rank + 1, self.file + 1),
               (self.rank, self.file - 1), (self.rank, self.file + 1),
               (self.rank - 1, self.file - 1), (self.rank - 1, self.file), (self.rank - 1, self.file + 1)]

        res = []

        for (rank, file) in pos:
            if rank > 7 or rank < 0:
                continue
            if file > 7 or file < 0:
                continue
            if state[rank][file].get_id() != '.' and state[rank][file].get_color() == self.color:
                continue
            res.append((rank, file))

        return res

    def get_id(self):
        return 'K'

if __name__ == '__main__':
    print('Piece Class')