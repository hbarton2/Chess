import pygame
import piece

nums = [0, 60, 120, 180, 240, 300, 360, 420]
horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['8', '7', '6', '5', '4', '3', '2', '1']

whitePawn = pygame.image.load("Images/whitePawn.png")
blackPawn = pygame.image.load("Images/blackPawn.png")
whiteBish = pygame.image.load("Images/whiteBishop.png")
blackBish = pygame.image.load("Images/blackBishop.png")
whiteKnight = pygame.image.load("Images/whiteKnight.png")
blackKnight = pygame.image.load("Images/blackKnight.png")
whiteRook = pygame.image.load("Images/whiteRook.png")
blackRook = pygame.image.load("Images/blackRook.png")
whiteQueen = pygame.image.load("Images/whiteQueen.png")
blackQueen = pygame.image.load("Images/blackQueen.png")
whiteKing = pygame.image.load("Images/whiteKing.png")
blackKing = pygame.image.load("Images/blackKing.png")


def init(screen):
    wpa = piece.Pawn(screen.blit(whitePawn, (0, 360)), whitePawn, 'w')
    wpb = piece.Pawn(screen.blit(whitePawn, (60, 360)), whitePawn, 'w')
    wpc = piece.Pawn(screen.blit(whitePawn, (120, 360)), whitePawn, 'w')
    wpd = piece.Pawn(screen.blit(whitePawn, (180, 360)), whitePawn, 'w')
    wpe = piece.Pawn(screen.blit(whitePawn, (240, 360)), whitePawn, 'w')
    wpf = piece.Pawn(screen.blit(whitePawn, (300, 360)), whitePawn, 'w')
    wpg = piece.Pawn(screen.blit(whitePawn, (360, 360)), whitePawn, 'w')
    wph = piece.Pawn(screen.blit(whitePawn, (420, 360)), whitePawn, 'w')
    bpa = piece.Pawn(screen.blit(blackPawn, (0, 60)), blackPawn, 'b')
    bpb = piece.Pawn(screen.blit(blackPawn, (60, 60)), blackPawn, 'b')
    bpc = piece.Pawn(screen.blit(blackPawn, (120, 60)), blackPawn, 'b')
    bpd = piece.Pawn(screen.blit(blackPawn, (180, 60)), blackPawn, 'b')
    bpe = piece.Pawn(screen.blit(blackPawn, (240, 60)), blackPawn, 'b')
    bpf = piece.Pawn(screen.blit(blackPawn, (300, 60)), blackPawn, 'b')
    bpg = piece.Pawn(screen.blit(blackPawn, (360, 60)), blackPawn, 'b')
    bph = piece.Pawn(screen.blit(blackPawn, (420, 60)), blackPawn, 'b')
    wk = piece.King(screen.blit(whiteKing, (240, 420)), whiteKing, 'w')
    wq = piece.Queen(screen.blit(whiteQueen, (180, 420)), whiteQueen, 'w')
    bk = piece.King(screen.blit(blackKing, (240, 0)), blackKing, 'b')
    bq = piece.Queen(screen.blit(blackQueen, (180, 0)), blackQueen, 'b')
    wra = piece.Rook(screen.blit(whiteRook, (0, 420)), whiteRook, 'w')
    wrh = piece.Rook(screen.blit(whiteRook, (420, 420)), whiteRook, 'w')
    wbc = piece.Bishop(screen.blit(whiteBish, (120, 420)), whiteBish, 'w')
    wbf = piece.Bishop(screen.blit(whiteBish, (300, 420)), whiteBish, 'w')
    wknb = piece.Knight(screen.blit(whiteKnight, (60, 420)), whiteKnight, 'w')
    wkng = piece.Knight(screen.blit(whiteKnight, (360, 420)), whiteKnight, 'w')
    bra = piece.Rook(screen.blit(blackRook, (0, 0)), blackRook, 'b')
    brh = piece.Rook(screen.blit(blackRook, (420, 0)), blackRook, 'b')
    bbc = piece.Bishop(screen.blit(blackBish, (120, 0)), blackBish, 'b')
    bbf = piece.Bishop(screen.blit(blackBish, (300, 0)), blackBish, 'b')
    bknb = piece.Knight(screen.blit(blackKnight, (60, 0)), blackKnight, 'b')
    bkng = piece.Knight(screen.blit(blackKnight, (360, 0)), blackKnight, 'b')

    gridArr = [[Square() for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            gridArr[i][j].set_y(nums[i])
            gridArr[i][j].set_x(nums[j])
            gridArr[i][j].set_algebraic(horizontal[j] + vertical[i])

    gridArr[0][0].set_contains(True, bra)
    gridArr[0][1].set_contains(True, bknb)
    gridArr[0][2].set_contains(True, bbc)
    gridArr[0][3].set_contains(True, bq)
    gridArr[0][4].set_contains(True, bk)
    gridArr[0][5].set_contains(True, bbf)
    gridArr[0][6].set_contains(True, bkng)
    gridArr[0][7].set_contains(True, brh)
    gridArr[1][0].set_contains(True, bpa)
    gridArr[1][1].set_contains(True, bpb)
    gridArr[1][2].set_contains(True, bpc)
    gridArr[1][3].set_contains(True, bpd)
    gridArr[1][4].set_contains(True, bpe)
    gridArr[1][5].set_contains(True, bpf)
    gridArr[1][6].set_contains(True, bpg)
    gridArr[1][7].set_contains(True, bph)
    gridArr[6][0].set_contains(True, wpa)
    gridArr[6][1].set_contains(True, wpb)
    gridArr[6][2].set_contains(True, wpc)
    gridArr[6][3].set_contains(True, wpd)
    gridArr[6][4].set_contains(True, wpe)
    gridArr[6][5].set_contains(True, wpf)
    gridArr[6][6].set_contains(True, wpg)
    gridArr[6][7].set_contains(True, wph)
    gridArr[7][0].set_contains(True, wra)
    gridArr[7][1].set_contains(True, wknb)
    gridArr[7][2].set_contains(True, wbc)
    gridArr[7][3].set_contains(True, wq)
    gridArr[7][4].set_contains(True, wk)
    gridArr[7][5].set_contains(True, wbf)
    gridArr[7][6].set_contains(True, wkng)
    gridArr[7][7].set_contains(True, wrh)

    return gridArr


class Board:
    def __init__(self, screen):
        self.board = init(screen)

    def get_at_cords(self, cords):
        for col in self.board:
            for item in col:
                if cords[0] in range(item.x, item.x + 60) and cords[1] in range(item.y, item.y + 60):
                    return item


class Square:
    def __init__(self, x=0, y=0, cont=False, contained=None, algebraic=''):
        self.x = x
        self.y = y
        self.cords = (x, y)
        self.contains = cont
        self.contained_piece = contained
        self.algebraic = algebraic

    def get_algebraic(self):
        return self.algebraic

    def set_algebraic(self, algebraic):
        self.algebraic = algebraic

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_contains(self, cont=False, contained=None):
        self.contains = cont
        self.contained_piece = contained
