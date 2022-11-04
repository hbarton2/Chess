import pygame
import grid
import piece

nums = [0, 60, 120, 180, 240, 300, 360, 420]
grey1 = [0, 120, 240, 360]
grey2 = [60, 180, 300, 420]
grey_squares = []
white = 255, 255, 255
grey = 80, 80, 80
horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['8', '7', '6', '5', '4', '3', '2', '1']
movable = pygame.image.load("Images/movable.png")

notation_arr = [[(0, 0, '') for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        notation_arr[i][j] = (nums[j], nums[i], horizontal[j] + vertical[i])

for i in grey1:
    for j in grey2:
        grey_squares.append((i, j))
        grey_squares.append((j, i))


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
        if item > 420 or item < 0 or (board.get_at_cords(cords) is not None and board.get_at_cords(cords).contains and
                                      board.get_at_cords(cords).contained_piece.color == color):
            value = False
    return value


def clear_square(cords, screen, board):
    color = white
    if cords in grey_squares:
        color = grey
    pygame.draw.rect(screen, color, pygame.Rect(cords[0], cords[1], 60, 60))
    if board.get_at_cords(cords).contains:
        ref_piece = board.get_at_cords(cords).contained_piece
        piece.ref = screen.blit(ref_piece.img, cords)


def between(cords, p1, p2):
    ret = False
    x = cords[0]
    y = cords[1]
    x1 = x3 = p1.get_x()
    y1 = y3 = p1.get_y()
    x2 = x4 = p2.get_x()
    y2 = y4 = p2.get_y()
    between_diagonal = []
    if x1 < x2 and y1 < y2:
        while x3 < x4 and y3 < y4:
            x3 += 60
            y3 += 60
            between_diagonal.append((x3, y3))
    elif x1 > x2 and y1 > y2:
        while x3 > x4 and y3 > y4:
            x3 -= 60
            y3 -= 60
            between_diagonal.append((x3, y3))
    elif y1 < y2 and x1 > x2:
        while y3 < y4 and x3 > x4:
            y3 += 60
            x3 -= 60
            between_diagonal.append((x3, y3))
    elif y1 > y2 and x1 < x2:
        while y3 > y4 and x3 < x4:
            y3 -= 60
            x3 += 60
            between_diagonal.append((x3, y3))
    if (x == x1 == x2 and (y1 < y < y2 or y1 > y > y2)) or \
            (y == y1 == y2 and (x1 < x < x2 or x1 > x > x2)) or \
            cords in between_diagonal:
        ret = True
    return ret
