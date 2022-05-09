import pygame

nums = [0, 60, 120, 180, 240, 300, 360, 420]
horizontal = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
vertical = ['8', '7', '6', '5', '4', '3', '2', '1']
movable = pygame.image.load("Images/movable.png")

notation_arr = [[(0, 0, '') for _ in range(8)] for _ in range(8)]
for i in range(8):
    for j in range(8):
        notation_arr[i][j] = (nums[j], nums[i], horizontal[j] + vertical[i])


def get_algebraic(cords):
    for col in notation_arr:
        for item in col:
            if item[0] == cords[0] and item[1] == cords[1]:
                return item[2]


def show_legal_moves(moves, board):



def is_valid(cords):
    value = True
    for item in cords:
        if item > 420 or item < 0:
            value = False
    return value


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
