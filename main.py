import pygame
import sys

import helpers
import piece
import grid

pygame.init()

size = width, height = 480, 480
white = 255, 255, 255
grey = 80, 80, 80
square2 = [420, 300, 180, 60]
square1 = [0, 120, 240, 360]

indicator = pygame.image.load("Images/squareOutline.png")

screen = pygame.display.set_mode(size)


def clear_board():
    screen.fill(grey)
    for i in square1:
        for j in square1:
            pygame.draw.rect(screen, white, pygame.Rect(i, j, 60, 60))
    for i in square2:
        for j in square2:
            pygame.draw.rect(screen, white, pygame.Rect(i, j, 60, 60))


clear_board()
moves_shown = False
piece_to_move = None
moves = []
board = grid.Board(screen)
check = False
checking_pieces = []
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
                    if check:
                        check = False
                        helpers.clear_square(board.get(turn, piece.King).get_cords(), screen, board)
                    if checking_pieces:
                        checking_pieces = []
                    if turn == 'w':
                        turn = 'b'
                    else:
                        turn = 'w'
                opp_king = board.get(turn, piece.King)
                if helpers.get_algebraic(opp_king.get_cords()) in piece_to_move.get_legal_moves(board):
                    checking_pieces.append(piece_to_move)
                    check = True
                for col in board.board:
                    for item in col:
                        if item.contains and type(item.contained_piece) == piece.Queen \
                                or type(item.contained_piece) == piece.Rook \
                                or type(item.contained_piece) == piece.Bishop:
                            if helpers.get_algebraic(opp_king.get_cords()) \
                                    in item.contained_piece.get_legal_moves(board) \
                                    and item.contained_piece not in checking_pieces:
                                checking_pieces.append(item.contained_piece)
                                check = True
                if check:
                    screen.blit(indicator, opp_king.get_cords())
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
                    temp_moves = []
                    if check and type(piece_to_move) != piece.King:
                        for item in checking_pieces:
                            for move in moves:
                                if move in moves and (helpers.between(helpers.cords_from_algebraic(move),
                                                                      item, board.get(turn, piece.King))) \
                                        or move == helpers.get_algebraic(item.get_cords()):
                                    temp_moves.append(move)
                        moves = temp_moves
                    if moves:
                        helpers.show_legal_moves(moves, board, screen)
                        moves_shown = True
