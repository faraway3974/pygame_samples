# handmade LCD font for pygame
# 5x7ドットマトリクス

from math import log
import pygame
from pygame.locals import Rect
from mcje.vec3 import Vec3
from mcje.minecraft import Minecraft
import param_MCJE as param
from param_MCJE import PLAYER_ORIGIN as po
import sys

mc = Minecraft.create(address=param.ADRS_MCR, port=param.PORT_MCR)
result = mc.setPlayer(param.PLAYER_NAME, po.x, po.y, po.z)
if ("Error" in result):
    sys.exit(result)
else:
    print(result)

with open("fonts/font.txt", encoding="utf-8") as f:
    LCD_font_styles = f.read().split('\n')

DARK_GRAY = (40, 40, 40)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (10, 250, 10)
YELLOW = (250, 250, 20)
WHITE = (250, 250, 250)


class LCD_font():
    def __init__(self, screen):
        self.screen = screen

    def init_col(self, BLOCK_SIZE=4, BLOCK_INTV=4, COLOR_ON=WHITE, COLOR_OFF=GRAY, BLOCK_ON=param.DIAMOND_BLOCK, BLOCK_OFF=param.AIR):
        # ひと桁、コラムの設定
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        self.BLOCK_SIZE = BLOCK_SIZE
        self.BLOCK_INTV = BLOCK_INTV
        # on/offのカラー
        self.COLOR_ON = COLOR_ON
        self.BLOCK_ON = BLOCK_ON
        self.COLOR_OFF = COLOR_OFF
        self.BLOCK_OFF = BLOCK_OFF

    def init_row(self, X_ORG=2, Y_ORG=8, COL_INTV=6, XMC_ORG=0, YMC_ORG=0):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG * self.BLOCK_INTV
        self.XMC_ORG = XMC_ORG
        self.Y_ORG = Y_ORG * self.BLOCK_INTV
        self.YMC_ORG = YMC_ORG
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV * self.BLOCK_INTV

    def update_col(self, col=0, code=2):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        block_size = self.BLOCK_SIZE
        i = 0
        for y in range(7):
            for x in range(5):
                if LCD_font_styles[code * 7 + y][x] == "1":
                    color = self.COLOR_ON
                    block = self.BLOCK_ON
                else:
                    color = self.COLOR_OFF
                    block = self.BLOCK_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                xmc = self.XMC_ORG + 6 * col
                y0 = self.Y_ORG
                ymc = self.YMC_ORG
                # ドットの原点座標
                org1 = (x0 + x * self.BLOCK_INTV, y0 + y * self.BLOCK_INTV)
                xmc0 = (xmc + x)
                ymc0 = (ymc + y -y -y)
                # ドットを描く
                pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], block_size, block_size))
                mc.setBlock(xmc0 -40, ymc0 +120, -20, block)
                i += 1

    def disp_num2(self, rjust=4, zfil=False, num=1234, base=16):
        # numをrjust桁で右詰め表示する。桁あふれが起きると、右にずれていく。
        # zfil==Trueの時、上位桁をゼロで埋める。Falseの場合は、ブランク表示。
        if num <= 0:
            num = 1
        num_cols = int(log(num, base)) + 1
        if num_cols > rjust:
            rjust = num_cols
        for disp_col in range(rjust):
            col = disp_col + num_cols - rjust
            if col >= 0:
                self.update_col(col=disp_col, num=num // (base ** (num_cols - col - 1)), base=base)
            else:
                if zfil is True:
                    self.update_col(col=disp_col, num=0)
                else:
                    self.update_col(col=disp_col, blank=True)
