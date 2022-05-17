import pygame
import grid
import piece

nums = [0, 60, 120, 180, 240, 300, 360, 420]
horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['8', '7', '6', '5', '4', '3', '2', '1']
movable = pygame.image.load("Images/movable.png")

notation_arr = [[(0, 0, '') for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        notation_arr[i][j] = (nums[j], nums[i], horizontal[j] + vertical[i])


def check_score(board):
    black_score = 0
    white_score = 0
    for col in board.board:
        for item in col:
            if item.contains and not type(item.contained_piece) == piece.King:
                if item.contained_piece.color == 'w':
                    white_score += item.contained_piece.points
                if item.contained_piece.color == 'b':
                    black_score += item.contained_piece.points
    return black_score, white_score


def get_algebraic(cords):
    for col in notation_arr:
        for item in col:
            if item[0] == cords[0] and item[1] == cords[1]:
                return item[2]


def cords_from_algebraic(algebraic):
    for col in notation_arr:
        for item in col:
            if item[2] == algebraic:
                return item[0], item[1]


def show_legal_moves(moves, board, screen):
    for alg in moves:
        screen.blit(movable, cords_from_algebraic(alg))


def is_valid(cords, color, board):
    value = True
    for item in cords:
        if item > 420 or item < 0 or (board.get_at_cords(cords).contains and
                                      board.get_at_cords(cords).contained_piece.color == color):
            value = False
    return value


def clear_square(cords, screen, board):
    pygame.draw.rect(screen, screen.get_at((cords[0], cords[1])),
                     pygame.Rect(cords[0], cords[1], 60, 60))
    if board.get_at_cords(cords).contains:
        ref_piece = board.get_at_cords(cords).contained_piece
        piece.ref = screen.blit(ref_piece.img, cords)


def remove_behind_left(cords, cord_list):
    for item in cord_list:
        if item[0] < cords[0] and item[1] == cords[1]:
            cord_list.remove(item)


def remove_behind_right(cords, cord_list):
    for item in cord_list:
        if item[0] > cords[0] and item[1] == cords[1]:
            cord_list.remove(item)


def remove_behind_down(cords, cord_list):
    for item in cord_list:
        if item[1] > cords[1] and item[0] == cords[0]:
            cord_list.remove(item)


def remove_behind_up(cords, cord_list):
    for item in cord_list:
        if item[1] < cords[1] and item[0] == cords[0]:
            cord_list.remove(item)
