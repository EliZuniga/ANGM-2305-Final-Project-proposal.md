import pygame
import sys

#this will be the constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = SQUARESIZE // 2 - 5
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50

#this will be the colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 255)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)

#this will be the gameboard
def create_board():
    board = []
    for _ in range(ROW_COUNT):
        row = [0] * COLUMN_COUNT
        board.append(row)
    return board

#Drop piece in the board
def drop_piece(board, row, col, piece):
    board[row][col] = piece

#This line will check is the column is valid
def is_valid_location(board, col):
    return board[0][col] == o