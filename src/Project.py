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
    return board[0][col] == 0

#This line will get next available row
def get_next_open_row(board, col):
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == 0:
            return r
        
#Will check for a win
def check_win(board, piece):
    # Horizontal check
    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # Vertical check
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Diagonal (down-right)
    for r in range(ROW_COUNT - 3):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
            
    # Diagnoal (up-rigth)
    for r in range(3, ROW_COUNT):
        for c in range(COLUMN_COUNT - 3):
            if board[r][c] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True
            
    return False

# Check if the board is full
def is_board_full(board):
    for col in range(COLUMN_COUNT):
        if board[0][col] == 0:
            return False
    return True

# Draw everything on the screen
def draw_board(board, screen, front, turn, message="", show_restart=False):
    screen.fill(BLACK)

    # This will show message or turn 
    if message:
        text = front.render(message, True, WHITE)
    else:
        text = front.render(f"Player {turn + 1}'s Turn", True, WHITE)
    screen.blit(text, (10 , 10))

    #Show restart button if needed 
    if show_restart:
        button_x = (COLUMN_COUNT * SQUARESIZE) // 2 + 100
        pygame.draw.rect(screen, GRAY, (button_x, 20, BUTTON_WIDTH, BUTTON_HEIGHT)) 
        restart_text = front.render("Restart" , True, BLACK)
        screen.blit(restart_text, (button_x + 35, 25))

    # Draw the board grid and pieces
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, (r + 1) * SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (c * SQUARESIZE + SQUARESIZE // 2, (r + 1) * SQUARESIZE + SQUARESIZE // 2), RADIUS)

    for r in range(ROW_COUNT):
        for c in range(COLUMN_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (c * SQUARESIZE + SQUARESIZE // 2, (r + 1) * SQUARESIZE + SQUARESIZE // 2), RADIUS)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, YELLOW, (c * SQUARESIZE + SQUARESIZE // 2, (r + 1) * SQUARESIZE + SQUARESIZE // 2), RADIUS)

    pygame.display.update()

# Reset game state
def reset_game():
    return create_board(), 0, False, ""

# Main game function 
def main():
    pygame.init()
    screen = pygame.display.set_mode((COLUMN_COUNT * SQUARESIZE, (ROW_COUNT + 1) * SQUARESIZE))
    pygame.display.set_caption("Connect Four")
    font = pygame.font.SysFont("monospace", 35)

    board, turn, game_over, message = reset_game()
    draw_board(board, screen, font, turn)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handel mouse click
            if event.typetype == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # This line will check if restart button was clicked
                if game_over:
                    button_x = (COLUMN_COUNT * SQUARESIZE) // 2 + 100