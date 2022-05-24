import pygame
import grid
import helpers


class Piece:
    def __init__(self, ref, img, color):
        self.ref = ref
        self.img = img
        self.color = color

    def get_x(self):
        return self.ref.x

    def get_y(self):
        return self.ref.y

    def get_cords(self):
        return self.get_x(), self.get_y()

    def move_piece(self, cords, screen, board):
        old = board.get_at_cords(self.get_cords())
        old.contains = False
        old.contained_piece = None
        pygame.draw.rect(screen, screen.get_at((cords[0], cords[1])), pygame.Rect(cords[0], cords[1], 60, 60))
        temp = screen.blit(self.img, cords)
        pygame.draw.rect(screen, screen.get_at((self.ref.x, self.ref.y)),
                         pygame.Rect(self.ref.x, self.ref.y, 60, 60))
        self.ref = temp
        pygame.display.flip()
        square = board.get_at_cords(cords)
        square.contains = True
        square.contained_piece = self
        for col in board.board:
            for item in col:
                if item.contains and type(item.contained_piece) == Pawn and item.contained_piece.en_passantable:
                    item.contained_piece.en_passantable = False
        return

    def get_legal_moves(self, board):
        return


class Pawn(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.en_passantable = False
        self.points = 1
        self.moved = False

    def move_piece(self, cords, screen, board):
        pre_move_x = self.get_x()
        to_move_contains = board.get_at_cords(cords).contains
        super().move_piece(cords, screen, board)
        if not self.en_passantable and not self.moved and \
                ((self.get_y() == 180 and self.color == 'b') or (self.get_y() == 240 and self.color == 'w')):
            self.en_passantable = True
        elif self.en_passantable and self.moved:
            self.en_passantable = False
        if not self.moved:
            self.moved = True
        if self.color == 'w' and cords[0] != pre_move_x and not to_move_contains \
                and board.get_at_cords((cords[0], cords[1] + 60)).contains \
                and type(board.get_at_cords((cords[0], cords[1] + 60)).contained_piece) == Pawn:
            square = board.get_at_cords((cords[0], cords[1] + 60))
            pygame.draw.rect(screen, screen.get_at((cords[0], cords[1] + 60)),
                             pygame.Rect(cords[0], cords[1] + 60, 60, 60))
            square.contains = False
            square.contained_piece = None
        if self.color == 'b' and cords[0] != pre_move_x and not to_move_contains \
                and board.get_at_cords((cords[0], cords[1] - 60)).contains \
                and type(board.get_at_cords((cords[0], cords[1] - 60)).contained_piece) == Pawn \
                and board.get_at_cords((cords[0], cords[1] - 60)).contained_piece.en_passantable:
            square = board.get_at_cords((cords[0], cords[1] - 60))
            helpers.clear_square((cords[0], cords[1] - 60), screen, board)
            square.contains = False
            square.contained_piece = None

    def get_legal_moves(self, board):
        potential_moves = []
        moves = []
        # holy_hell is potential moves for en passant (the name is a meme)
        holy_hell = [(self.get_x() + 60, self.get_y()), (self.get_x() - 60, self.get_y())]
        if self.color == 'w':
            takes = [(self.get_x() + 60, self.get_y() - 60), (self.get_x() - 60, self.get_y() - 60)]
            if board.get_at_cords((self.get_x(), self.get_y() - 60)) is not None and \
                    not board.get_at_cords((self.get_x(), self.get_y() - 60)).contains:
                potential_moves.append((self.get_x(), self.get_y() - 60))
                if not self.moved and not board.get_at_cords((self.get_x(), self.get_y() - 120)).contains:
                    potential_moves.append((self.get_x(), self.get_y() - 120))
            for cords in takes:
                if helpers.is_valid(cords, self.color, board) and board.get_at_cords(cords).contains \
                        and board.get_at_cords(cords).contained_piece.color != self.color:
                    potential_moves.append(cords)
            if self.get_y() == 180:
                for cords in holy_hell:
                    if board.get_at_cords(cords).contains \
                            and type(board.get_at_cords(cords).contained_piece) == Pawn \
                            and board.get_at_cords(cords).contained_piece.color != self.color \
                            and not board.get_at_cords((cords[0], cords[1] - 60)).contains \
                            and board.get_at_cords(cords).contained_piece.en_passantable:
                        new_cords = (cords[0], cords[1] - 60)
                        potential_moves.append(new_cords)
        if self.color == 'b':
            diagonals = [(self.get_x() + 60, self.get_y() + 60), (self.get_x() - 60, self.get_y() + 60)]
            if not board.get_at_cords((self.get_x(), self.get_y() + 60)).contains:
                potential_moves.append((self.get_x(), self.get_y() + 60))
                if not self.moved and not board.get_at_cords((self.get_x(), self.get_y() + 120)).contains:
                    potential_moves.append((self.get_x(), self.get_y() + 120))
            for cords in diagonals:
                if helpers.is_valid(cords, self.color, board) and board.get_at_cords(cords).contains \
                        and board.get_at_cords(cords).contained_piece.color != self.color:
                    potential_moves.append(cords)
            if self.get_y() == 240:
                for cords in holy_hell:
                    if board.get_at_cords(cords).contains and board.get_at_cords(cords).contained_piece.points == 1 \
                            and board.get_at_cords(cords).contained_piece.color != self.color \
                            and not board.get_at_cords((cords[0], cords[1] + 60)).contains \
                            and board.get_at_cords(cords).contained_piece.en_passantable:
                        new_cords = (cords[0], cords[1] + 60)
                        potential_moves.append(new_cords)
        for cords in potential_moves:
            if helpers.is_valid(cords, self.color, board):
                moves.append(helpers.get_algebraic(cords))
        return moves


class Bishop(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 3

    def get_legal_moves(self, board):
        x = x1 = x2 = x3 = self.get_x()
        y = y1 = y2 = y3 = self.get_y()
        potential_moves = []
        moves = []
        while x < 420 and y < 420:
            x += 60
            y += 60
            potential_moves.append((x, y))
            if board.get_at_cords((x, y)).contains:
                break
        while x1 < 420 and y1 > 0:
            x1 += 60
            y1 -= 60
            potential_moves.append((x1, y1))
            if board.get_at_cords((x1, y1)).contains:
                break
        while x2 > 0 and y2 < 420:
            x2 -= 60
            y2 += 60
            potential_moves.append((x2, y2))
            if board.get_at_cords((x2, y2)).contains:
                break
        while x3 > 0 and y3 > 0:
            x3 -= 60
            y3 -= 60
            potential_moves.append((x3, y3))
            if board.get_at_cords((x3, y3)).contains:
                break
        for cords in potential_moves:
            if helpers.is_valid(cords, self.color, board):
                moves.append(helpers.get_algebraic(cords))
        return moves


class Knight(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 3

    def get_legal_moves(self, board):
        x = self.get_x()
        y = self.get_y()
        moves = []
        potential_moves = [(x + 120, y + 60), (x + 120, y - 60), (x - 120, y + 60), (x - 120, y - 60),
                           (x + 60, y + 120), (x - 60, y + 120), (x + 60, y - 120), (x - 60, y - 120)]
        for cords in potential_moves:
            if helpers.is_valid(cords, self.color, board):
                moves.append(helpers.get_algebraic(cords))
        return moves


class Rook(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 5
        self.moved = False

    def move_piece(self, cords, screen, board):
        super().move_piece(cords, screen, board)
        if not self.moved:
            self.moved = True

    def get_legal_moves(self, board):
        x = x1 = x2 = self.get_x()
        y = y1 = y2 = self.get_y()
        potential_moves = []
        moves = []
        # Best way I could find to make sure moves past a piece aren't being used
        while y1 <= 360:
            y1 += 60
            potential_moves.append((x, y1))
            if board.get_at_cords((x, y1)).contains:
                break
        while y2 >= 60:
            y2 -= 60
            potential_moves.append((x, y2))
            if board.get_at_cords((x, y2)).contains:
                break
        while x1 <= 360:
            x1 += 60
            potential_moves.append((x1, y))
            if board.get_at_cords((x1, y)).contains:
                break
        while x2 >= 60:
            x2 -= 60
            potential_moves.append((x2, y))
            if board.get_at_cords((x2, y)).contains:
                break
        for cords in potential_moves:
            if helpers.is_valid(cords, self.color, board):
                moves.append(helpers.get_algebraic(cords))
        return moves


class Queen(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 9

    # Queen uses Bishop and Rook moves to get its own (nice time saver)
    def get_legal_moves(self, board):
        moves = []
        for cords in Bishop.get_legal_moves(self, board):
            moves.append(cords)
        for cords in Rook.get_legal_moves(self, board):
            moves.append(cords)
        return moves


class King(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.moved = False

    def move_piece(self, cords, screen, board):
        super().move_piece(cords, screen, board)
        if not self.moved:
            self.moved = True

    def get_legal_moves(self, board):
        x = self.get_x()
        y = self.get_y()
        moves = []
        potential_moves = [(x + 60, y), (x - 60, y), (x, y + 60), (x, y - 60),
                           (x + 60, y + 60), (x + 60, y - 60),
                           (x - 60, y + 60), (x - 60, y - 60)]
        cant_moves = []
        for cords in potential_moves:
            if helpers.is_valid(cords, self.color, board):
                moves.append(helpers.get_algebraic(cords))
        for col in board.board:
            for item in col:
                if item.contains and item.contained_piece is not None and item.contained_piece.color != self.color:
                    if type(item.contained_piece) == Queen or type(item.contained_piece) == Knight:
                        cant_moves.append(item.contained_piece.get_legal_moves(board))
                    if type(item.contained_piece) == Rook and (item.x in range(self.get_x() - 60, self.get_x() + 60) or
                                                               item.y in range(self.get_y() - 60, self.get_x() + 60)):
                        cant_moves.append(item.contained_piece.get_legal_moves(board))
                    if type(item.contained_piece) == Bishop and (item.x > self.get_x() + 120
                                                                 or item.contained_piece.get_x() < self.get_x() - 120
                                                                 or item.y > self.get_y() + 120
                                                                 or item.y < self.get_y() - 120):
                        cant_moves.append(item.contained_piece.get_legal_moves(board))
                    if type(item.contained_piece) == Pawn and item.x in range(self.get_x() - 60, self.get_x() + 60):
                        if self.color == 'w' and self.get_y() - 180 < item.y < self.get_y():
                            cant_moves.append(item.contained_piece.get_legal_moves(board))
                        if self.color == 'b' and self.get_y() + 180 > item.y > self.get_y():
                            cant_moves.append(item.contained_piece.get_legal_moves(board))
                    if type(item.contained_piece) == King:
                        x = item.x
                        y = item.y
                        potential_moves2 = [(x + 60, y), (x - 60, y), (x, y + 60), (x, y - 60),
                                            (x + 60, y + 60), (x + 60, y - 60),
                                            (x - 60, y + 60), (x - 60, y - 60)]
                        for cords in potential_moves2:
                            if helpers.get_algebraic(cords) in moves:
                                moves.remove(helpers.get_algebraic(cords))
                    for move in moves:
                        for move_list in cant_moves:
                            if move in move_list:
                                moves.remove(move)
        return moves
