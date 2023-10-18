import pygame
from const import *

class Game:
    def __init__(self):
        pass

    def show_bg(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = BOARD_LIGHT_COLOR
                else:
                    color = BOARD_DARK_COLOR

                rect = (col *  SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)
                pygame.draw.rect(screen, color, rect)