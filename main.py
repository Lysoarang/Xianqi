from tkinter import Tk
from classes.board import Board
from classes.game_ui import GameUI

if __name__ == '__main__':
    root = Tk()
    board = Board()
    game = GameUI(root, board)
    root.mainloop()