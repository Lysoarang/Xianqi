from classes.piece import Piece

class Soldier(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'Soldier')

    def get_valid_moves(self, board):
        moves = []
        directions = {'red': [(-1, 0)], 'black': [(1, 0)]}
        if (self.color == 'red' and 9 - self.x >= 5) or (self.color == 'black' and self.x >= 5):
            directions = {
            'red': [(-1, 0), (0,-1), (0, 1)],
            'black': [(1, 0), (0,-1), (0, 1)]
            }
        for dx, dy in directions[self.color]:
            new_x, new_y  = self.x + dx, self.y + dy
            if 0 <= new_x <= 9 and 0 <= new_y <= 8:
                if board.grid[new_x][new_y] is None or board.grid[new_x][new_y].color != self.color:
                    moves.append((new_x, new_y))
        return moves