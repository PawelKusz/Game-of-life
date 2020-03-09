class Game:
    COLUMNS = 20
    ROWS = 30
    board = None

    player = 1

    game_over = False
    winner = 0

    def __init__(self):
        self.init_board()

    def init_board(self):
        self.board = []
        for r in range(self.ROWS):
            row = []
            for c in range(self.COLUMNS):
                row.append(0)
            self.board.append(row)

    def how_many_neighbors(self, row, col):
        result = 0
        for r in range(-1, 2):
            for c in range(-1, 2):
                if r == 0 and c == 0:
                    continue
                row2 = (row + r) % self.ROWS
                col2 = (col + c) % self.COLUMNS
                result += self.board[row2][col2]
        return result

    def clear(self):
        for r in range(self.ROWS):
            for c in range(self.COLUMNS):
                self.board[r][c] = 0

    def next_generation(self):
        board = []
        for r in range(self.ROWS):
            row = []
            for c in range(self.COLUMNS):
                neighbors = self.how_many_neighbors(r,c)
                current = self.board[r][c]

                value = 0
                if current == 1:
                    if neighbors == 2 or neighbors == 3:
                        value = 1
                    else:
                        value = 0
                else :
                    if neighbors == 3:
                        value = 1
                    else:
                        value = 0

                row.append(value)
            board.append(row)

        self.board = board
