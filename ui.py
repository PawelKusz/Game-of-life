from tkinter import *
from functools import partial
from game import *


playing = False

class InfoFrame(Frame):
    def __init__(self, game, board_frame):
        super().__init__()

        self.game = game
        self.board_frame = board_frame

        self.play_text = StringVar()
        self.play_text.set('Play')
        self.play_button = None

        self.initUI()

    def next_generation(self):
        if not playing:
            self.board_frame.show_next_generation()
            self.play_text.set("Play")

    def restart(self):
        global playing
        self.game.clear()
        self.board_frame.update_board()
        playing = False

    def play_stop(self):
        global playing
        if playing:
            playing = False
            self.play_text.set("Play")
        else:
            playing = True
            self.board_frame.start()
            self.play_text.set("Stop")

    def initUI(self):
        self.pack(fill=BOTH, expand=True)

        self.play_button = Button(self, textvariable=self.play_text, command=self.play_stop)
        self.play_button.pack(padx=15)
        b = Button(self, text='Next generatiom', command=self.next_generation)
        b.pack(padx=15)
        b = Button(self, text='Restart', command=self.restart)
        b.pack(padx=15)


class BoardFrame(Frame):
    def __init__(self, game):
        super().__init__()

        self.game = game
        self.padding = 5

        self.info_frame = None

        self.board = None
        self.initUI()


    def initUI(self):
        self.pack(fill=BOTH, expand=True)
        self.init_board()
        self.update_board()


    def set_info_frame(self, info_frame):
        self.info_frame = info_frame

    def clear(self):
        self.update_board()

    def show_next_generation(self):
        self.game.next_generation()
        self.update_board()

    def start(self):
        if not playing:
            return
        self.show_next_generation()
        self.after(100, self.start)

    def change_color(self,row, col, event):
        if playing:
            return
        color = self.board[row][col].cget('bg')
        if color == 'black':
            color = 'white'
            value = 0
        else:
            color = 'black'
            value = 1
        self.board[row][col].configure(bg=color)
        self.game.board[row][col] = value


    def init_board(self):
        if self.board is None:
            self.board = []
            for r in range(self.game.ROWS):
                self.board.append([])
                frame = Frame(self)
                frame.pack()
                for c in range(self.game.COLUMNS):
                    square = Canvas(frame, bg='white', width=16, height=16)
                    square.row = r
                    square.col = c
                    func = partial(self.change_color, r, c)
                    square.bind("<Button-1>", func)
                    square.pack(side=LEFT)
                    self.board[r].append(square)

    def update_board(self):
        for r in range(self.game.ROWS):
            for c in range(self.game.COLUMNS):
                if self.game.board[r][c] == 0:
                    color = 'white'
                else:
                    color = 'black'
                self.board[r][c].configure(bg=color)


class MainWindow(Tk):

    def __init__(self):
        super().__init__()
        self.title("4 in row")
        self.resizable(False, False)

        self.game = Game()
        self.initUI()

    def initUI(self):

        board_frame = BoardFrame(self.game)
        board_frame.pack(side=LEFT)

        info_frame = InfoFrame(self.game, board_frame)
        board_frame.set_info_frame(info_frame)



def main():
    root = MainWindow()

    root.mainloop()


if __name__ == '__main__':
    main()
