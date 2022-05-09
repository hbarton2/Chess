import pygame
import sys
import piece
import grid

pygame.init()

size = width, height = 480, 480
black = 0, 0, 0
white = 255, 255, 255
grey = 80, 80, 80
square2 = [420, 300, 180, 60]
square1 = [0, 120, 240, 360]

screen = pygame.display.set_mode(size)

screen.fill(grey)
for i in square1:
    for j in square1:
        pygame.draw.rect(screen, white, pygame.Rect(i, j, 60, 60))
for i in square2:
    for j in square2:
        pygame.draw.rect(screen, white, pygame.Rect(i, j, 60, 60))

board = grid.Board(screen)

while 1:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            square_clicked = board.get_at_cords(event.pos)
            if square_clicked.contains:
                legal_moves = square_clicked.contained_piece.get_legal_moves(board)
