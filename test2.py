from datetime import datetime
import pygame
from lcd_font_pg1 import LCD_font as LCD_font_pg
from lcd_font_mc1 import LCD_font as LCD_font_mc
from mcje.vec3 import Vec3
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
from time import sleep

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
CYAN = (120, 120, 250)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 320])
pygame.display.set_caption("Clock and Timer")
screen.fill(DARK_GRAY)

display1 = LCD_font_mc(screen)
display1.init_col(BLOCK_SIZE=9, BLOCK_INTV=10, COLOR_ON=RED, COLOR_OFF=GRAY, BLOCK_ON=param.DIAMOND_BLOCK, BLOCK_OFF=param.AIR)
display1.init_row(X_ORG=1, Y_ORG=1, COL_INTV=6, XMC_ORG=0, YMC_ORG=0)

display2 = LCD_font_mc(screen)
display2.init_col(BLOCK_SIZE=9, BLOCK_INTV=10, COLOR_ON=RED, COLOR_OFF=GRAY, BLOCK_ON=param.DIAMOND_BLOCK, BLOCK_OFF=param.AIR)
display2.init_row(X_ORG=1, Y_ORG=11, COL_INTV=6, XMC_ORG=0, YMC_ORG=-9)

running = True
while running:
    dt_now = datetime.now()

    display1.update_col(col=0, code=ord(str(dt_now.hour // 10)))
    display1.update_col(col=1, code=ord(str(dt_now.hour % 10)))
    display1.update_col(col=2, code=ord(':'))
    display1.update_col(col=3, code=ord(str(dt_now.minute // 10)))
    display1.update_col(col=4, code=ord(str(dt_now.minute % 10)))
    display1.update_col(col=5, code=ord(':'))
    display1.update_col(col=6, code=ord(str(dt_now.second // 10)))
    display1.update_col(col=7, code=ord(str(dt_now.second % 10)))

    display2.update_col(col=0, code=ord(str(dt_now.year // 1000)))
    display2.update_col(col=1, code=ord(str((dt_now.year % 1000) // 100)))
    display2.update_col(col=2, code=ord(str(((dt_now.year % 1000) % 100) // 10)))
    display2.update_col(col=3, code=ord(str((((dt_now.year % 1000) % 100) % 10))))
    display2.update_col(col=4, code=ord('-'))
    display2.update_col(col=5, code=ord(str(dt_now.month // 10)))
    display2.update_col(col=6, code=ord(str(dt_now.month % 10)))
    display2.update_col(col=7, code=ord('-'))
    display2.update_col(col=8, code=ord(str(dt_now.day // 10)))
    display2.update_col(col=9, code=ord(str(dt_now.day % 10)))

    pygame.display.update()
    clock.tick(20)
    screen.fill(DARK_GRAY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if not running:
            break

pygame.quit()