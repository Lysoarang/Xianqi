import math
import tkinter as tk
from PIL import Image, ImageTk
from classes.piece import Piece

cell_size = 80
piece_size = 60
earthy_orange = '#D0882C'
dark_brown = '#803300'
WIDTH = 740
HEIGHT = 820
river_words = ['楚', '河', '漢', '界']

class GameUI:
    def __init__(self, root, board):
        # Initialize the interface
        self.root = root
        self.root.title('Xiangqi')

        # Get screen's size
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate the position so that the window is in the middle of the screen
        x_position = (screen_width - WIDTH) // 2
        y_position = (screen_height - HEIGHT) // 2

        # Set window's position
        root.geometry(f'{WIDTH}x{HEIGHT}+{x_position}+{y_position}')
        
        self.board = board
        self.selected_piece = None
        self.turn = 'r'

        # Create a canvas to draw board
        self.canvas = tk.Canvas(self.root, width = WIDTH, height = HEIGHT, bg = dark_brown)
        self.canvas.pack()

        # Load images
        self.piece_images = self.load_piece_images()

        # Catch mouse's click event
        self.canvas.bind('<Button-1>', self.on_click)

        # Draw
        self.draw_board()

    def draw_board(self):
        self.canvas.delete('all')
        self.draw_grid()
        self.draw_pieces()

    def draw_cross_marks(self, x, y):
        col = 50 + x * cell_size
        row = 50 + y * cell_size
        dis = 7
        if y == 0:
            self.canvas.create_line(row + dis, col - dis * 2, row + dis, col - dis, width = 2)
            self.canvas.create_line(row + dis, col - dis, row + dis * 2, col - dis, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis, col + dis * 2, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis * 2, col + dis, width = 2)
        elif y == 8:
            self.canvas.create_line(row - dis, col - dis * 2, row - dis, col - dis, width = 2)
            self.canvas.create_line(row - dis, col - dis, row - dis * 2, col - dis, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis, col + dis * 2, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis * 2, col + dis, width = 2)
        else:
            self.canvas.create_line(row - dis, col - dis * 2, row - dis, col - dis, width = 2)
            self.canvas.create_line(row - dis, col - dis, row - dis * 2, col - dis, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis, col + dis * 2, width = 2)
            self.canvas.create_line(row - dis, col + dis, row - dis * 2, col + dis, width = 2)
            self.canvas.create_line(row + dis, col - dis * 2, row + dis, col - dis, width = 2)
            self.canvas.create_line(row + dis, col - dis, row + dis * 2, col - dis, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis, col + dis * 2, width = 2)
            self.canvas.create_line(row + dis, col + dis, row + dis * 2, col + dis, width = 2)

    def draw_grid(self):
        self.canvas.create_rectangle(50, 50, WIDTH - 50, HEIGHT - 50, fill = earthy_orange)
        for i in range(10):
            self.canvas.create_line(50, 50 + cell_size * i, WIDTH - 50, 50 + cell_size * i, width = 2)
        for j in range(9):
            if j == 0 or j == 8:
                self.canvas.create_line(50 + cell_size * j, 50, 50 + cell_size * j, HEIGHT - 50, width = 2)
            else:
                self.canvas.create_line(50 + cell_size * j, 50, 50 + cell_size * j, HEIGHT - 50 - 5 * cell_size, width = 2)
                self.canvas.create_line(50 + cell_size * j, HEIGHT - 50 - 4 * cell_size, 50 + cell_size * j, HEIGHT - 50, width = 2)
        self.canvas.create_line(WIDTH - 50 - 5 * cell_size, 50, WIDTH - 50 - 3 * cell_size, HEIGHT - 50 - 7 * cell_size, width = 2)
        self.canvas.create_line(WIDTH - 50 - 3 * cell_size, 50, WIDTH - 50 - 5 * cell_size, HEIGHT - 50 - 7 * cell_size, width = 2)
        self.canvas.create_line(WIDTH - 50 - 5 * cell_size, HEIGHT - 50 - 2 * cell_size, WIDTH - 50 - 3 * cell_size, HEIGHT - 50, width = 2)
        self.canvas.create_line(WIDTH - 50 - 3 * cell_size, HEIGHT - 50 - 2 * cell_size, WIDTH - 50 - 5 * cell_size, HEIGHT - 50, width = 2)

        self.draw_cross_marks(2, 1)
        self.draw_cross_marks(2, 7)
        self.draw_cross_marks(3, 0)
        self.draw_cross_marks(3, 2)
        self.draw_cross_marks(3, 4)
        self.draw_cross_marks(3, 6)
        self.draw_cross_marks(3, 8)
        self.draw_cross_marks(7, 1)
        self.draw_cross_marks(7, 7)
        self.draw_cross_marks(6, 0)
        self.draw_cross_marks(6, 2)
        self.draw_cross_marks(6, 4)
        self.draw_cross_marks(6, 6)
        self.draw_cross_marks(6, 8)
        
        self.canvas.create_text(50 + cell_size + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[0],
                                font = ('Arial', 50), fill = 'black')
        self.canvas.create_text(50 + cell_size * 2 + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[1],
                                font = ('Arial', 50), fill = 'black')
        self.canvas.create_text(50 + cell_size * 5 + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[2],
                                font = ('Arial', 50), fill = 'black')
        self.canvas.create_text(50 + cell_size * 6 + cell_size // 2, 50 + 4 * cell_size + cell_size // 2, text = river_words[3],
                                font = ('Arial', 50), fill = 'black')
        
    def load_piece_images(self):
        types = [
            'Soldier', 'Horse', 'Elephant', 'Advisor', 'General', 'Cannon', 'Chariot'
        ]
        colors = ['r', 'b']
        images = {}
        for color in colors:
            for type in types:
                path = f'assets/{color}_{type}.png'
                try:
                    img = Image.open(path).resize((piece_size, piece_size))
                    images[f'{color}_{type}'] = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f'Error when loading image {path}: {e}')
        return images
    
    def draw_pieces(self):
        for i in range(10):
            for j in range(9):
                piece = self.board.grid[i][j]
                if piece:
                    key = f'{piece.color}_{piece.type}'
                    if key in self.piece_images:
                        self.canvas.create_image(50 + j * cell_size, 50 + i * cell_size, 
                                                 image = self.piece_images[key], anchor = 'center')

    def on_click(self, event):
        # event.x,y are click's position
        col = math.floor((event.x - 50 + cell_size // 2) / cell_size)
        row = math.floor((event.y - 50 + cell_size // 2) / cell_size)
        if 0 <= row < 10 and 0 <= col < 9:
            piece = self.board.grid[row][col]
            if self.selected_piece:
                if self.is_valid_move(self.selected_piece, row, col):
                    self.move_piece(self.selected_piece, row, col)
                else:
                    if piece and piece.color == self.selected_piece.color:
                        self.selected_piece = piece
            else:
                if piece:
                    if piece.color == self.turn:
                        self.selected_piece = piece
                    else:
                        print('Not your turn!')

    def is_valid_move(self, piece, row, col):
        return (row, col) in piece.get_valid_moves(self.board)

    def move_piece(self, piece, row, col):
        self.board.grid[piece.x][piece.y] = None  
        piece.x, piece.y = row, col  
        self.board.grid[row][col] = piece  
        self.selected_piece = None  
        self.turn = 'b' if self.turn == 'r' else 'r'
        self.draw_board()