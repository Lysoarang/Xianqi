from classes.piece import Piece

class Soldier(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'Soldier')
    
    def get_valid_moves(self, board):
        moves = []
        bf_directions = [(1, 0), (-1, 0)]
        at_directions = [(1, 0), (0, 1), (0, -1)]
        