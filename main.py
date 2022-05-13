import pygame
import sys

import helpers
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

moves_shown = False
piece_to_move = None
moves = []
board = grid.Board(screen)
white_score = 39
black_score = 39
turn = 'w'

while 1:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            square_clicked = board.get_at_cords(event.pos)
            if moves_shown and piece_to_move is not None and moves:
                if square_clicked.get_algebraic() in moves:
                    piece_to_move.move_piece((square_clicked.x, square_clicked.y), screen, board)
                    if turn == 'w':
                        turn = 'b'
                    else:
                        turn = 'w'
                for item in moves:
                    if item != square_clicked.get_algebraic():
                        helpers.clear_square(helpers.cords_from_algebraic(item), screen, board)
                moves = []
                moves_shown = False
                piece_to_move = None
                black_score, white_score = helpers.check_score(board)
            elif not moves_shown:
                if square_clicked.contains and square_clicked.contained_piece.color == turn:
                    piece_to_move = square_clicked.contained_piece
                    moves = piece_to_move.get_legal_moves(board)
                    if moves:
                        helpers.show_legal_moves(moves, board, screen)
                        moves_shown = True

