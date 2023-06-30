
class Piece:

    def __init__(self, rank, file, color):
        self.rank = rank      # 0 - 7
        self.file = file      # 0 - 7
        self.color = color    # 'W' or 'B'

    def get_location(self):
        return (self.rank, self.file)

    def get_moves(self, state):
        return []

    def move(self, rank, file):
        self.rank = rank
        self.file = file

    def get_id(self):
        return 'T'

    def get_color(self):
        return self.color


class Blank(Piece):

    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)

    def get_id(self):
        return '.'


class Pawn(Piece):

    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)
        self.first_move = True

    def get_moves(self, state):
        res = []
        if state[self.rank, self.file + 1] == '.':
            res.append((self.rank, self.file + 1))

        if self.first_move and state[self.rank, self.file + 2] == '.':
            res.append((self.rank, self.file + 2))

        return res

    def move(self, rank, file):
        self.rank = rank
        self.file = file
        self.first_move = False

    def get_id(self):
        return 'P'


class Knight(Piece):

    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)

    def get_moves(self, state):

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
            if state[rank, file].get_id() != '.' and state[rank, file].get_color() == self.color:
                continue
            res.append((rank, file))

        return res

    def get_id(self):
        return 'N'


class Bishop(Piece):

    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)

    def get_moves(self, state):

        res = []

        # up-right diagonal
        up = 1
        right = 1
        while (self.rank + up <= 7 and self.file + right <= 7):

            if state[self.rank + up, self.file + right].get_id() == '.':
                res.append((self.rank + up, self.file + right))
                up += 1
                right += 1
                continue

            if state[self.rank + up, self.file + right].get_color() != self.color:
                res.append((self.rank + up, self.file + right))

            break

        # up-left diagonal
        up = 1
        left = -1
        while (self.rank + up <= 7 and self.file + left >= 0):

            if state[self.rank + up, self.file + left].get_id() == '.':
                res.append((self.rank + up, self.file + left))
                up += 1
                left -= 1
                continue

            if state[self.rank + up, self.file + left].get_color() != self.color:
                res.append((self.rank + up, self.file + left))

            break

        # down-right diagonal
        down = -1
        right = 1
        while (self.rank + down >= 0 and self.file + right <= 7):

            if state[self.rank + down, self.file + right].get_id() == '.':
                res.append((self.rank + down, self.file + right))
                down -= 1
                right += 1
                continue

            if state[self.rank + down, self.file + right].get_color() != self.color:
                res.append((self.rank + down, self.file + right))

            break

        # down-left diagonal
        down = -1
        left = -1
        while (self.rank + down >= 0 and self.file + left >= 0):

            if state[self.rank + down, self.file + left].get_id() == '.':
                res.append((self.rank + down, self.file + left))
                down -= 1
                left -= 1
                continue

            if state[self.rank + down, self.file + left].get_color() != self.color:
                res.append((self.rank + down, self.file + left))

            break

        return res

    def get_id(self):
        return 'B'


class Rook(Piece):

    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)

    def get_moves(self, state):

        res = []

        # looking right
        pos_file = self.file + 1
        while (pos_file <= 7):
            if state[self.rank, pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file += 1
            elif state[self.rank, pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank, pos_file].get_color() == self.color:
                break

        # looking left
        pos_file = self.file - 1
        while (pos_file >= 0):
            if state[self.rank, pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file -= 1
            elif state[self.rank, pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank, pos_file].get_color() == self.color:
                break

        # looking up
        pos_rank = self.rank + 1
        while (pos_rank <= 7):
            if state[pos_rank, self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank += 1
            elif state[pos_rank, self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank, self.rank].get_color() == self.color:
                break

        # looking down
        pos_rank = self.rank + 1
        while (pos_rank >= 0):
            if state[pos_rank, self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank -= 1
            elif state[pos_rank, self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank, self.rank].get_color() == self.color:
                break

        return res

    def get_id(self):
        return 'R'


class Queen(Piece):

    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)

    def get_moves(self, state):

        res = []

        # up-right diagonal
        up = 1
        right = 1
        while (self.rank + up <= 7 and self.file + right <= 7):

            if state[self.rank + up, self.file + right].get_id() == '.':
                res.append((self.rank + up, self.file + right))
                up += 1
                right += 1
                continue

            if state[self.rank + up, self.file + right].get_color() != self.color:
                res.append((self.rank + up, self.file + right))

            break

        # up-left diagonal
        up = 1
        left = -1
        while (self.rank + up <= 7 and self.file + left >= 0):

            if state[self.rank + up, self.file + left].get_id() == '.':
                res.append((self.rank + up, self.file + left))
                up += 1
                left -= 1
                continue

            if state[self.rank + up, self.file + left].get_color() != self.color:
                res.append((self.rank + up, self.file + left))

            break

        # down-right diagonal
        down = -1
        right = 1
        while (self.rank + down >= 0 and self.file + right <= 7):

            if state[self.rank + down, self.file + right].get_id() == '.':
                res.append((self.rank + down, self.file + right))
                down -= 1
                right += 1
                continue

            if state[self.rank + down, self.file + right].get_color() != self.color:
                res.append((self.rank + down, self.file + right))

            break

        # down-left diagonal
        down = -1
        left = -1
        while (self.rank + down >= 0 and self.file + left >= 0):

            if state[self.rank + down, self.file + left].get_id() == '.':
                res.append((self.rank + down, self.file + left))
                down -= 1
                left -= 1
                continue

            if state[self.rank + down, self.file + left].get_color() != self.color:
                res.append((self.rank + down, self.file + left))

            break

        # looking right
        pos_file = self.file + 1
        while (pos_file <= 7):
            if state[self.rank, pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file += 1
            elif state[self.rank, pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank, pos_file].get_color() == self.color:
                break

        # looking left
        pos_file = self.file - 1
        while (pos_file >= 0):
            if state[self.rank, pos_file].get_id() == '.':
                res.append((self.rank, pos_file))
                pos_file -= 1
            elif state[self.rank, pos_file].get_color() != self.color:
                res.append((self.rank, pos_file))
                break
            elif state[self.rank, pos_file].get_color() == self.color:
                break

        # looking up
        pos_rank = self.rank + 1
        while (pos_rank <= 7):
            if state[pos_rank, self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank += 1
            elif state[pos_rank, self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank, self.rank].get_color() == self.color:
                break

        # looking down
        pos_rank = self.rank + 1
        while (pos_rank >= 0):
            if state[pos_rank, self.rank].get_id() == '.':
                res.append((pos_rank, self.rank))
                pos_rank -= 1
            elif state[pos_rank, self.rank].get_color() != self.color:
                res.append((pos_rank, self.rank))
                break
            elif state[pos_rank, self.rank].get_color() == self.color:
                break

        return res

    def get_id(self):
        return 'Q'


class King(Piece):

    def __init__(self, rank, file, color):
        super().__init__(rank, file, color)

    def get_moves(self, state):

        pos = [(self.rank + 1, self.file - 1), (self.rank + 1, self.file), (self.rank + 1, self.file + 1),
               (self.rank, self.file - 1), (self.rank, self.file + 1),
               (self.rank - 1, self.file - 1), (self.rank - 1, self.file), (self.rank - 1, self.file + 1)]

        res = []

        for (rank, file) in pos:
            if rank > 7 or rank < 0:
                continue
            if file > 7 or file < 0:
                continue
            if state[rank, file].get_id() != '.' and state[rank, file].get_color() == self.color:
                continue
            res.append((rank, file))

    def get_id(self):
        return 'K'

if __name__ == '__main__':
    print('Piece Class')