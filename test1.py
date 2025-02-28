from datetime import datetime
import pygame
from lcd_font_pg1 import LCD_font

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([400, 320])
pygame.display.set_caption("Clock and Timer")
screen.fill(DARK_GRAY)

display1 = LCD_font(screen)
display1.init_col(BLOCK_SIZE=9, BLOCK_INTV=10, COLOR_ON=RED, COLOR_OFF=GRAY)
display1.init_row(X_ORG=1, Y_ORG=1, COL_INTV=6)

running = True
while running:
    dt_now = datetime.now()
    code = int(dt_now.hour // 10
               + dt_now.hour % 10
               + dt_now.minute // 10
               + dt_now.minute % 10
               + dt_now.second // 10
               + dt_now.second % 10)
    display1.update_col(col=0, code=code)

    pygame.display.update()
    clock.tick(20)
    screen.fill(DARK_GRAY)

pygame.quit()