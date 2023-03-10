import sys

import math
import pygame
from data.autotile import map_to_auto
from data.tile import Tile, ImageTile

def generate_map(group, map, engroup, game):
    global lowest, t
    for y,row in enumerate(map):
        for x,tile in enumerate(row):
            if tile == 1:
                t = Tile((x*50,y*50), group)
                lowest = t
            elif tile == 2:
                t = Enemy((x*50,y*50), engroup, group)
                lowest = t
            elif tile == 3:
                t = ImageTile((x * 50, y * 50), group, 'data/grass.png')
                lowest = t


    return lowest


class Bulllet(pygame.sprite.Sprite):
    def __init__(self, pos, group, tilegroup, dir, glbullets):
        super().__init__()
        self.image = pygame.Surface((10,10))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        group.add(self)
        tilegroup.add(self)
        glbullets.add(self)
        self.dir = dir
        self.colimage = pygame.Surface((12,12))
        self.colrect = self.colimage.get_rect(center=self.rect.center)
        self.deflected = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, tilegroup):
        super().__init__()
        self.pos = pos
        self.image = pygame.image.load('data/enemy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(topleft=pos)
        group.add(self)
        tilegroup.add(self)
        self.shoottimer = 120
        self.bullets = pygame.sprite.Group()
        self.tilegroup = tilegroup
        self.alive = True

    def shoot(self, target, screen, shield, tiles, enemies, glbullets, game):
        self.pos = self.rect.center
        self.shoottimer -= 1
        if self.shoottimer <= 0:
            self.shoottimer = 120
            rad = math.atan2(target.rect.centery - self.rect.centery, target.rect.centerx - self.rect.centerx)
            dirx = round(math.cos(rad) *5)
            diry = round(math.sin(rad) *5)
            #print(f'{dirx}:{diry}')


            Bulllet(self.pos, self.bullets, self.tilegroup, [dirx, diry], glbullets)
            self.shoottimer = 120


        self.bullets.draw(screen)
        for b in self.bullets:

            b.colrect.center = b.rect.center
            if b.rect.y > 750:
                b.kill()
            elif b.rect.y < 0:
                b.kill()
            elif b.rect.x < 0:
                b.kill()
            elif b.rect.x > 1000:
                b.kill()

            if target.rect.colliderect(b.colrect):
                game.score -= 1000
                game.tiles.empty()
                game.enemies.empty()
                game.map, game.startPos, game.lowest = map_to_auto(game.map)
                game.player.rect.y = game.startPos[1] - 1000
                game.player.rect.x = game.startPos[0]
                game.lowest = generate_map(game.tiles, game.map, game.enemies, game)
            if shield.rect.colliderect(b.colrect):
                b.deflected = True
                mpos = pygame.mouse.get_pos()
                rad = shield.rad
                rad = math.atan2(mpos[1] - b.rect.y, mpos[0] - b.rect.x)
                dirx = round(math.cos(rad) * 5)
                diry = round(math.sin(rad) * 5)
                b.dir[0] = dirx
                b.dir[1] = diry
                b.rect.x += dirx * 2
                b.rect.y += diry * 2

                b.colrect.x += dirx * 2
                b.colrect.y += diry * 2

            if not self.alive:
                b.kill()

            if self.rect.colliderect(b.rect) and b.deflected:
                game.score += int(math.hypot(target.rect.centery - self.rect.centery,
                                         target.rect.centerx - self.rect.centerx))
                b.kill()
                for b in self.bullets:
                    b.kill()
                self.remove(tiles, enemies)
                self.alive = False

            b.rect.x += b.dir[0]
            b.rect.y += b.dir[1]
            b.colrect.x += b.dir[0]
            b.colrect.y += b.dir[1]

        for gb in glbullets:
            if self.rect.colliderect(gb.rect) and gb.deflected:
                game.score += int(math.hypot(target.rect.centery - self.rect.centery,
                                         target.rect.centerx - self.rect.centerx))
                gb.kill()
                for b in self.bullets:
                    b.kill()
                self.remove(tiles, enemies)
                self.alive = False





