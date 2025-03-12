from classes.board import Board
from classes.piece import Piece

if __name__ == '__main__':
    board = Board()
    print(board)

    for i in range(10):
        for j in range(9):
            piece : Piece = board.grid[i][j]
            if piece:
                print(piece.__class__.__name__, piece.get_valid_moves(board))