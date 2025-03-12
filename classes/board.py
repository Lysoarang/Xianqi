from classes.piece import Piece

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(9)] for _ in range(10)]
        self.setup_peice()

    def __str__(self):
        return '\n'.join(['|'.join([j.type if j else '__' for j in i]) for i in self.grid])

    def setup_peice(self):
        self.grid[0][0] = Piece(0, 0, 'black', 'Chariot')
        self.grid[0][1] = Piece(0, 1, 'black', 'Horse')
        self.grid[0][2] = Piece(0, 2, 'black', 'Elephant')
        self.grid[0][3] = Piece(0, 3, 'black', 'Advisor')
        self.grid[0][4] = Piece(0, 4, 'black', 'General')
        self.grid[0][5] = Piece(0, 5, 'black', 'Advisor')
        self.grid[0][6] = Piece(0, 6, 'black', 'Elephant')
        self.grid[0][7] = Piece(0, 7, 'black', 'Horse')
        self.grid[0][8] = Piece(0, 8, 'black', 'Chariot')
        self.grid[2][1] = Piece(2, 1, 'black', 'Cannon')
        self.grid[2][7] = Piece(2, 7, 'black', 'Cannon')
        self.grid[3][0] = Piece(3, 0, 'black', 'Soldier')
        self.grid[3][2] = Piece(3, 2, 'black', 'Soldier')   
        self.grid[3][4] = Piece(3, 4, 'black', 'Soldier')
        self.grid[3][6] = Piece(3, 6, 'black', 'Soldier')
        self.grid[3][8] = Piece(3, 8, 'black', 'Soldier')
        self.grid[9][0] = Piece(9, 0, 'red', 'Chariot')
        self.grid[9][1] = Piece(9, 1, 'red', 'Horse')
        self.grid[9][2] = Piece(9, 2, 'red', 'Elephant')
        self.grid[9][3] = Piece(9, 3, 'red', 'Advisor')
        self.grid[9][4] = Piece(9, 4, 'red', 'General')
        self.grid[9][5] = Piece(9, 5, 'red', 'Advisor')
        self.grid[9][6] = Piece(9, 6, 'red', 'Elephant')
        self.grid[9][7] = Piece(9, 7, 'red', 'Horse')
        self.grid[9][8] = Piece(9, 8, 'red', 'Chariot')
        self.grid[7][1] = Piece(7, 1, 'red', 'Cannon')
        self.grid[7][7] = Piece(7, 7, 'red', 'Cannon')
        self.grid[6][0] = Piece(6, 0, 'red', 'Soldier')
        self.grid[6][2] = Piece(6, 2, 'red', 'Soldier')
        self.grid[6][4] = Piece(6, 4, 'red', 'Soldier')
        self.grid[6][6] = Piece(6, 6, 'red', 'Soldier')
        self.grid[6][8] = Piece(6, 8, 'red', 'Soldier')
        
    def print_board(self):
        for i in self.grid:
            print('|'.join([j.type if j else '__' for j in i]))
            print('-' * 40)
