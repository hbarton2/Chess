import pygame
import grid
import helpers


class Piece:
    def __init__(self, ref, img, color):
        self.ref = ref
        self.img = img
        self.color = color
        self.moved = False

    def get_x(self):
        return self.ref.x

    def get_y(self):
        return self.ref.y

    def get_cords(self):
        return self.ref.y, self.ref.y

    def move_piece(self, cords, screen, board):
        old = board.get_at_cords(self.get_cords())
        old.contains = False
        old.contained_piece = None
        if board.get_at_cords(cords).contains:
            pygame.draw.rect(screen, screen.get_at((cords[0], cords[1])),
                             pygame.Rect(cords[0], cords[1], 60, 60))
        temp = screen.blit(self.img, cords)
        pygame.draw.rect(screen, screen.get_at((self.ref.x, self.ref.y)),
                         pygame.Rect(self.ref.x, self.ref.y, 60, 60))
        self.ref = temp
        pygame.display.flip()
        if not self.moved:
            self.moved = True
        square = board.get_at_cords(cords)
        square.contains = True
        square.contained_piece = self
        return

    def get_legal_moves(self, board):
        return


class Pawn(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.en_passantable = False
        self.points = 1

    def move_piece(self, cords, screen, board):
        super().move_piece(cords, screen, board)
        if self.en_passantable:
            self.en_passantable = False
        if not self.en_passantable and not self.moved:
            self.en_passantable = True

    def get_legal_moves(self, board):
        potential_moves = []
        moves = []
        holy_hell = [(self.get_x() + 60, self.get_y()), (self.get_x() - 60, self.get_y())]
        if self.color == 'w':
            takes = [(self.get_x() + 60, self.get_y() - 60), (self.get_x() - 60, self.get_y() - 60)]
            if board.get_at_cords((self.get_x(), self.get_y() - 60)) is not None and \
                    not board.get_at_cords((self.get_x(), self.get_y() - 60)).contains:
                potential_moves.append((self.get_x(), self.get_y() - 60))
                if not self.moved and not board.get_at_cords((self.get_x(), self.get_y() - 120)).contains:
                    potential_moves.append((self.get_x(), self.get_y() - 120))
            for cords in takes:
                if helpers.is_valid(cords) and board.get_at_cords(cords).contains \
                        and board.get_at_cords(cords).contained_piece.color != self.color:
                    potential_moves.append(cords)
            #if self.get_y() == 180:
            #    for cords in holy_hell:
            #        if board.get_at_cords(cords).contains and board.get_at_cords(cords).contained_piece.points == 1 \
            #                and board.get_at_cords(cords).contained_piece.color != self.color \
            #                and not board.get_at_cords((cords[0], cords[1] - 60)).contains \
            #                and board.get_at_cords(cords).contained_piece.en_passantable:
            #            new_cords = (cords[0], cords[1] - 60)
            #            potential_moves.append(new_cords)
            for cords in potential_moves:
                if helpers.is_valid(cords):
                    moves.append(helpers.get_algebraic(cords))
        if self.color == 'b':
            diagonals = [(self.get_x() + 60, self.get_y() + 60), (self.get_x() - 60, self.get_y() + 60)]
            if not board.get_at_cords((self.get_x(), self.get_y() + 60)).contains:
                potential_moves.append((self.get_x(), self.get_y() + 60))
                if not self.moved and not board.get_at_cords((self.get_x(), self.get_y() + 120)).contains:
                    potential_moves.append((self.get_x(), self.get_y() + 120))
            for cords in diagonals:
                if helpers.is_valid(cords) and board.get_at_cords(cords).contains \
                        and board.get_at_cords(cords).contained_piece.color != self.color:
                    potential_moves.append(cords)
            #if self.get_y() == 240:
            #    for cords in holy_hell:
            #        if board.get_at_cords(cords).contains and board.get_at_cords(cords).contained_piece.points == 1 \
            #                and board.get_at_cords(cords).contained_piece.color != self.color \
            #                and not board.get_at_cords((cords[0], cords[1] + 60)).contains \
            #                and board.get_at_cords(cords).contained_piece.en_passantable:
            #            new_cords = (cords[0], cords[1] + 60)
            #            potential_moves.append(new_cords)
            for cords in potential_moves:
                if helpers.is_valid(cords):
                    moves.append(helpers.get_algebraic(cords))
        return moves


class Bishop(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 3


class Knight(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 3


class Rook(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 5


class Queen(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)
        self.points = 9


class King(Piece):
    def __init__(self, ref, img, color):
        super().__init__(ref, img, color)

