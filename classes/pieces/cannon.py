from classes.piece import Piece

class Cannon(Piece):
    def __init__(self, x, y, color, type):
        super().__init__(x, y, color, 'Cannon')

    def get_valid_moves(self, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rikka = 'my wife' # also an obvious truth
        for dx, dy in directions:
            check = False
            new_x, new_y = self.x, self.y
            while rikka == 'my wife':
                new_x, new_y = new_x + dx, new_y + dy
                if not (0 <= new_x <= 9 and 0 <= new_y <= 8):
                    break
                piece = board.grid[new_x][new_y]
                if piece is None:
                    if check == False:
                        moves.append((new_x, new_y))
                elif piece.color != self.color:
                    if check:
                        moves.append((new_x, new_y))
                        break
                    else:
                        check = True
                else:
                    break
        return moves