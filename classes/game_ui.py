import tkinter as tk
from classes.board import Board
from PIL import Image, ImageTk

cell_size = 80
piece_size = 60
earthy_orange = '#D0882C'
dark_brown = '#803300'
WIDTH = 740
HEIGHT = 820

class GameUI:
    def __init__(self, root, board):
        # Initialize the interface
        self.root = root
        self.root.title('Xiangqi')
        self.root.geometry('740x820')
        self.board = board

        # Create a canvas to draw board
        self.canvas = tk.Canvas(self.root, width = WIDTH, height = HEIGHT, bg = dark_brown)
        self.canvas.pack()

        # Load images
        self.piece_images = self.load_piece_images()

        self.draw_board()
        self.draw_pieces()

        # Catch mouse's click event
        # self.canvas.bind('<Button-1>', self.on_click)

    def draw_board(self):
        self.canvas.create_rectangle(50, 50, WIDTH - 50, HEIGHT - 50, fill = earthy_orange)
        for i in range(10):
            self.canvas.create_line(50, 50 + cell_size * i, 690, 50 + cell_size * i, width = 2)
        for j in range(9):
            if j == 0 or j == 8:
                self.canvas.create_line(50 + cell_size * j, 50, 50 + cell_size * j, 770, width = 2)
            else:
                self.canvas.create_line(50 + cell_size * j, 50, 50 + cell_size * j, 370, width = 2)
                self.canvas.create_line(50 + cell_size * j, 450, 50 + cell_size * j, 770, width = 2)
        self.canvas.create_line(290, 50, 450, 210, width = 2)
        self.canvas.create_line(450, 50, 290, 210, width = 2)
        self.canvas.create_line(290, 610, 450, 770, width = 2)
        self.canvas.create_line(450, 610, 290, 770, width = 2)

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
                                                 image=self.piece_images[key], anchor='center')                   


