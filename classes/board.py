from classes.piece import Piece
from classes.pieces import *


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(9)] for _ in range(10)]
        self.setup_peice()

    def __str__(self):
        return '\n'.join(['|'.join([j.type if j else '__' for j in i]) for i in self.grid])

    def create_piece(self, x, y, color, type):
        match type:
            case 'Soldier':
                self.grid[x][y] = Soldier(x, y, color, 'Soldier')
            case 'Horse':
                self.grid[x][y] = Horse(x, y, color, 'Horse')
            case 'Elephant':
                self.grid[x][y] = Elephant(x, y, color, 'Elephant')
            case 'Advisor':
                self.grid[x][y] = Advisor(x, y, color, 'Advisor')
            case 'General':
                self.grid[x][y] = General(x, y, color, 'General')
            case 'Cannon':
                self.grid[x][y] = Cannon(x, y, color, 'Cannon')
            case 'Chariot':
                self.grid[x][y] = Chariot(x, y, color, 'Chariot')
            case _:
                raise ValueError('Invalid piece type')
            
    def setup_peice(self):
        self.create_piece(0, 0, 'black', 'Chariot')
        self.create_piece(0, 1, 'black', 'Horse')
        self.create_piece(0, 2, 'black', 'Elephant')
        self.create_piece(0, 3, 'black', 'Advisor')
        self.create_piece(0, 4, 'black', 'General')
        self.create_piece(0, 5, 'black', 'Advisor')
        self.create_piece(0, 6, 'black', 'Elephant')
        self.create_piece(0, 7, 'black', 'Horse')
        self.create_piece(0, 8, 'black', 'Chariot')
        self.create_piece(2, 1, 'black', 'Cannon')
        self.create_piece(2, 7, 'black', 'Cannon')
        self.create_piece(3, 0, 'black', 'Soldier')
        self.create_piece(3, 2, 'black', 'Soldier')
        self.create_piece(3, 4, 'black', 'Soldier')
        self.create_piece(3, 6, 'black', 'Soldier')
        self.create_piece(3, 8, 'black', 'Soldier') 
        self.create_piece(9, 0, 'red', 'Chariot')
        self.create_piece(9, 1, 'red', 'Horse')
        self.create_piece(9, 2, 'red', 'Elephant')
        self.create_piece(9, 3, 'red', 'Advisor')
        self.create_piece(9, 4, 'red', 'General')
        self.create_piece(9, 5, 'red', 'Advisor')
        self.create_piece(9, 6, 'red', 'Elephant')
        self.create_piece(9, 7, 'red', 'Horse')
        self.create_piece(9, 8, 'red', 'Chariot')
        self.create_piece(7, 1, 'red', 'Cannon')
        self.create_piece(7, 7, 'red', 'Cannon')
        self.create_piece(6, 0, 'red', 'Soldier')
        self.create_piece(6, 2, 'red', 'Soldier')
        self.create_piece(6, 4, 'red', 'Soldier')
        self.create_piece(6, 6, 'red', 'Soldier')
        self.create_piece(6, 8, 'red', 'Soldier')
        
    def print_board(self):
        for i in self.grid:
            print('|'.join([j.type if j else '__' for j in i]))
            print('-' * 40)
