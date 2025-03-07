import pygame
from pygame.locals import Rect
from lcd_font_pg1 import LCD_font

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init

class disp_meg():
    def __init__(self, text):
        self.text = text
    
    def 