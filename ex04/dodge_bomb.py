import pygame as pg
import random
import sys
import tkinter.messagebox as tkm


def check_bound(obj_rct, scr_rct):
    # 第1引数：こうかとんrectまたは爆弾rect
    # 第2引数：スクリーンrect
    # 範囲内：+1／範囲外：-1
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate

def check_bound(obj_rct, scr_rct):
    yoko2, tate2 = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko2 = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate2 = -1
    return yoko2, tate2


def main():
    i = 1000
    clock =pg.time.Clock()
    # 練習１
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600, 900))
    scrn_rct = scrn_sfc.get_rect()
    pgbg_sfc = pg.image.load("fig/11.jpg")
    pgbg_rct = pgbg_sfc.get_rect()

    # 練習３
    tori_sfc = pg.image.load("fig/6.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400
    # scrn_sfcにtori_rctに従って，tori_sfcを貼り付ける
    scrn_sfc.blit(tori_sfc, tori_rct) 
    
    #ダミーボールの追加
    bo_sfc = pg.Surface((20, 20))
    bo_sfc.set_colorkey((255, 255, 255))
    pg.draw.circle(bo_sfc, (255, 0, 0), (10, 10), 10)
    bo_rct = bo_sfc.get_rect()
    bo_rct.centerx = random.randint(0, scrn_rct.width)
    bo_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bo_sfc, bo_rct) 
    vx2, vy2 = +1, +1

    # 練習５
    bomb_sfc = pg.Surface((20, 20)) # 正方形の空のSurface
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(0, scrn_rct.width)
    bomb_rct.centery = random.randint(0, scrn_rct.height)
    scrn_sfc.blit(bomb_sfc, bomb_rct) 
    vx, vy = +1, +1

    # 練習２
    while True:
        scrn_sfc.blit(pgbg_sfc, pgbg_rct) 

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # 練習4
        key_dct = pg.key.get_pressed() # 辞書型
        if key_dct[pg.K_UP] == True:
            tori_rct.centery -= 1
        if key_dct[pg.K_DOWN] == True:
            tori_rct.centery += 1
        if key_dct[pg.K_LEFT] == True:
            tori_rct.centerx -= 1
        if key_dct[pg.K_RIGHT] == True:
            tori_rct.centerx += 1
        # 8, k, u, oのキーでも移動できる
        if key_dct[pg.K_8]: 
            tori_rct.centery -= 1
        if key_dct[pg.K_k]:
            tori_rct.centery += 1
        if key_dct[pg.K_u]:
            tori_rct.centerx -= 1
        if key_dct[pg.K_o]:
            tori_rct.centerx += 1

        if key_dct[pg.K_s]:#sを押すと強制終了
            return
            
        if check_bound(tori_rct, scrn_rct) != (True, True):
        
            # どこかしらはみ出ていたら
            if key_dct[pg.K_UP] == True:
                tori_rct.centery += 1
            if key_dct[pg.K_DOWN] == True:
                tori_rct.centery -= 1
            if key_dct[pg.K_LEFT] == True:
                tori_rct.centerx += 1
            if key_dct[pg.K_RIGHT] == True:
                tori_rct.centerx -= 1


                       
        scrn_sfc.blit(tori_sfc, tori_rct) 

        # 練習６        
        bomb_rct.move_ip(vx, vy)
        scrn_sfc.blit(bomb_sfc, bomb_rct) 
        yoko, tate = check_bound(bomb_rct, scrn_rct)
        vx *= yoko
        vy *= tate
        if yoko == False:#壁にあたるとスピードがあがる
            vx*=-1.2
        if tate == False:
            vy*=-1.2

        bo_rct.move_ip(vx, vy)
        scrn_sfc.blit(bo_sfc, bo_rct) 
        yoko2, tate2 = check_bound(bo_rct, scrn_rct)
        vx2 *= yoko2
        vy2 *= tate2
        if yoko == False:
            vx*=-1.35
        if tate == False:
            vy*=-1.35
        
    
        if tori_rct.colliderect(bomb_rct): #ゲームオーバー時にウィンドウを表示
            txt ="ゲームオーバー"
            tkm.showinfo(txt,f"[{txt}]です")
            return

        #練習８
        if tori_rct.colliderect(bomb_rct):
            return

        pg.display.update()
        clock.tick(i)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()