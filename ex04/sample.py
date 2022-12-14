import pygame as pg
import sys


def main():
    clock = pg.time.Clock()


    pg.display.set_caption("初めてのPyGame")
    scrn_sfc = pg.display.set_mode((800,600))

    tori_sfc = pg.image.load("fig/6.png") 
    tori_sfc = pg.transform.rotozoom(tori_sfc,90,2.0) 
    tori_rct = tori_sfc.get_rect() 
    tori_rct = 400, 300 
    scrn_sfc.blit(tori_sfc, tori_rct)
    #scrn_sfcにtori_rctに従って、tori_fscを貼り付ける   

    pg.display.update()
    clock.tick(1)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit() 
    sys.exit()