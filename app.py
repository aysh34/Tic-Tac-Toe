import numpy as np
import pygame
import math

circle = pygame.image.load("circle.png")
cancle = pygame.image.load("cancel.png")

# board 3x3
board = np.zeros((3, 3))


def isValidMark(r, c):
    return board[r][c] == 0  # weather its already marked or not


def mark(r, c, player):  # mark the specific cell
    board[r][c] = player  # player can be 1 or 2


def isBoardFull():  # indicates the end of the game
    for rows in range(3):
        for cols in range(3):
            if board[rows][cols] == 0:
                return False
    return True


def drawBoard():
    for r in range(3):
        for c in range(3):
            if board[r][c] == 1:
                window.blit(circle, ((c * 200) + 50, (r * 200) + 50))
            elif board[r][c] == 2:
                window.blit(cancle, ((c * 200) + 50, (r * 200) + 50))
    pygame.display.update()


def drawLines():
    # vertical lines
    pygame.draw.line(window, (0, 0, 0), (200, 0), (200, 600), 10)
    pygame.draw.line(window, (0, 0, 0), (400, 0), (400, 600), 10)
    # horizontal lines
    pygame.draw.line(window, (0, 0, 0), (0, 200), (600, 200), 10)
    pygame.draw.line(window, (0, 0, 0), (0, 400), (600, 400), 10)


def isWinningMove(player):
    color = (
        (0, 0, 255) if player == 1 else (255, 0, 0)
    )  # Blue for Player 1, Red for Player 2

    # Horizontal check
    for r in range(3):
        if board[r][0] == player and board[r][1] == player and board[r][2] == player:
            pygame.draw.line(
                window, color, (10, (r * 200) + 100), (590, (r * 200) + 100), 10
            )
            return True

    # Vertical check
    for c in range(3):
        if board[0][c] == player and board[1][c] == player and board[2][c] == player:
            pygame.draw.line(
                window, color, ((c * 200) + 100, 10), ((c * 200) + 100, 590), 10
            )
            return True

    # Diagonal checks
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        pygame.draw.line(window, color, (10, 10), (590, 590), 10)
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        pygame.draw.line(window, color, (590, 10), (10, 590), 10)
        return True

    return False


gameOver = False
turn = 0
pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")
window.fill((255, 255, 255))
drawLines()
pygame.display.update()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # Ensures clean exit

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

            # Calculate row and column
            r = event.pos[1] // 200
            c = event.pos[0] // 200

            # Determine whose turn it is
            if turn % 2 == 0:  # Player 1
                if isValidMark(r, c):
                    mark(r, c, 1)
                    if isWinningMove(1):
                        gameOver = True
                else:
                    turn -= 1  # Give another chance
            else:  # Player 2
                if isValidMark(r, c):
                    mark(r, c, 2)
                    if isWinningMove(2):
                        gameOver = True
                else:
                    turn -= 1  # Give another chance

            # Check if the board is full before updating turn
            if isBoardFull():
                gameOver = True
            else:
                turn += 1  # Only increment turn if game isn't over

            print(board)
            drawBoard()

    if gameOver:
        print("Game Over")
        pygame.time.wait(2000)

        # Wait for the user to click to restart
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False  # Exit loop on click

        # Reset board and screen
        board.fill(0)
        window.fill((255, 255, 255))
        drawLines()
        drawBoard()
        gameOver = False
        pygame.display.update()
