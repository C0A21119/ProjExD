import os
import sys

import pygame as pg

from random import randint


main_dir = os.path.split(os.path.abspath(__file__))[0]

# 画面の表示
class Screen:
    
    def __init__(self, title, width_height, background_image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(width_height)
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(background_image)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

# こうかとんの表示
class Bird:
    
    key_delta = {
        pg.K_UP:    [0, -1],#矢印のキーで上下左右に移動
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
        pg.K_w:     [0, -1],#w,a,s,dのキーで上下左右に移動
        pg.K_s:     [0, +1],
        pg.K_a:     [+1, 0],
        pg.K_d:     [-1, 0],
        pg.K_x:     [+1, +1],#x,z,e,qで斜め移動
        pg.K_z:     [-1, +1],
        pg.K_e:     [+1, -1],
        pg.K_q:     [-1, -1]
    }

    def __init__(self, img, zoom, xy):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, zoom)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr:Screen):
        key_states = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_states[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
                # 練習7
                if check_bound(self.rct, scr.rct) != (+1, +1):
                    self.rct.centerx -= delta[0]
                    self.rct.centery -= delta[1]
        self.blit(scr)

# 爆弾の表示
class Bomb:

    def __init__(self, color, rad, vxy, scr:Screen):
        self.sfc = pg.Surface((rad*2, rad*2)) 
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (rad,rad), rad) 
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.rct.move_ip(self.vx, self.vy) # 練習6
        self.blit(scr)

class Items:

        def __init__(self, color, rad, vxy, scr:Screen):
            self.sfc = pg.Surface((rad*2, rad*2)) 
            self.sfc.set_colorkey((0, 0, 0)) 
            pg.draw.circle(self.sfc, color, (rad,rad), rad) 
            self.rct = self.sfc.get_rect()
            self.rct.centerx = randint(0, scr.rct.width)
            self.rct.centery = randint(0, scr.rct.height)
            self.vx, self.vy = vxy # 練習6

        def blit(self, scr:Screen):
            scr.sfc.blit(self.sfc, self.rct)
    
        def update(self, scr:Screen):
            yoko, tate = check_bound(self.rct, scr.rct)
            self.vx *= yoko
            self.vy *= tate
            self.rct.move_ip(self.vx, self.vy) # 練習6
            self.blit(scr)

# 敵の表示
class Enemy:

    def __init__(self, enemy_image, xy, rad):
        self.sfc = pg.image.load(enemy_image)
        self.rct = self.sfc.get_rect()
        self.rct.center = xy
        self.vx, self.vy = rad

    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.vx += 0.009
        self.vy += 0.009
        self.rct.move_ip(self.vx, self.vy) # 練習6
        self.blit(scr)

# gameoverクラス
class GameOver:

    def __init__(self, title, width_height, background_image, kokaton_image, tori_location):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(width_height)
        self.rct = self.sfc.get_rect()
        self.bg_sfc = pg.image.load(background_image)
        self.bg_rct = self.bg_sfc.get_rect()
        self.tori_sfc = pg.image.load(kokaton_image)
        self.tori_sfc = pg.transform.rotozoom(self.tori_sfc, 0, 4.0)
        self.tori_rct = self.tori_sfc.get_rect()
        self.tori_rct.center = tori_location

    def blit(self):
        self.sfc.blit(self.bg_sfc, self.bg_rct)
        self.sfc.blit(self.tori_sfc, self.tori_rct)


class Shot():

    def __init__(self, color, rad, vxy, scr:Screen, bird:Bird):
        self.sfc = pg.Surface((rad*2, rad*2))
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (rad, rad), rad) 
        self.rct = self.sfc.get_rect()
        self.rct.centerx = randint(0, scr.rct.width)
        self.rct.centery = randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6
    
    def blit(self, scr:Screen):
        scr.sfc.blit(self.sfc, self.rct)
    
    def update(self, scr:Screen):
        self.vx = +1
        self.vy = +1
        self.rct.move_ip(self.vx, self.vy) # 練習6
        self.blit(scr)


def check_bound(obj_rct, scr_rct):
    """
    obj_rct：こうかとんrct，または，爆弾rct
    scr_rct：スクリーンrct
    領域内：+1／領域外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: 
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: 
        tate = -1
    return yoko, tate

# 画像の読み込み
def load_image(file):
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()

# 音の追加
def load_sound(file):
    if not pg.mixer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound(file)
        return sound
    except pg.error:
        print("Warning, unable to load, %s" % file)
    return None

# gameover画面の追加
def gameover():
    g_scr = GameOver("GameOver", (1600, 900), "fig/gameover.png", "fig/ghostbirads.png", (800, 450))
    clock = pg.time.Clock()
    while True:
        g_scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_state = pg.key.get_pressed()
        if key_state[pg.K_c]: # 終了ボタン
            main()
            return
        if key_state[pg.K_ESCAPE]:
            return
        pg.display.update()
        clock.tick(1000)


def main():
    # 練習1
    scr = Screen("負けるな！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    # 練習3
    tori = Bird("fig/6.png", 2.0, (900, 400))
    # 練習5
    bomb = Bomb((255, 0, 0), 10, (+1, +1), scr)          #爆弾
    eney = Enemy("fig/12.png", (50, 40), (+1, +1))       #敵
    shot = Shot((255, 255, 255), 10, (+1, +1), scr, tori)
    boom_sound = load_sound("boom.wav")                  #音
    tem = Items((255, 0, 0), 10, (+1, +1), scr)          #アイテム

    # 練習1
    clock = pg.time.Clock() 
    while True:
        scr.blit()
        # 練習2
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                return

        tori.update(scr)
        bomb.update(scr)
        eney.update(scr)
        tem.update(scr)

        key_state = pg.key.get_pressed()
        if   key_state[pg.K_SPACE]:
            shot.update(scr)

        boom_sound.play()
        # 練習8
        if tori.rct.colliderect(bomb.rct):
            gameover()
            return
        
        if tori.rct.colliderect(bomb.rct):
            gameover()
            return    
        
        if tori.rct.colliderect(eney.rct):
            gameover()
            return

        pg.display.update() #練習2
        clock.tick(1000)


if __name__ == "__main__":
    pg.init() # 初期化
    main()    # ゲームの本体
    pg.quit() # 初期化の解除
    sys.exit()