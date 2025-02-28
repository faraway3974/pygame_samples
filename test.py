import pygame
from lcd_font_pg1 import LCD_font

GRAY = (80, 80, 80)
GREEN = (10, 250, 10)


if __name__ == "__main__":
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 640

    pygame.init()
    screen1 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("LCD font")

    clock = pygame.time.Clock()

    lcd1 = LCD_font(screen1)
    lcd1.init_col(BLOCK_SIZE=7, BLOCK_INTV=8, COLOR_ON=GREEN, COLOR_OFF=GRAY)
    lcd1.init_row(X_ORG=8, Y_ORG=8, COL_INTV=6)

    for n in range(12):
        lcd1.update_col(col=n - 1, code=n)
    pygame.display.flip()  # update



    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(5)