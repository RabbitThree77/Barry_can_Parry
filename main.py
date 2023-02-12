import sys

import pygame
from player import Shield, Player
from Generate_Map import generate_map
from autotile import map_to_auto
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 750),)
        pygame.display.set_caption('Barry can Parry')
        self.clock = pygame.time.Clock()

        self.pshield = Shield()

        self.tiles = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.gloabalBullets = pygame.sprite.Group()

        # self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        #             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]]
        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
        self.mapid = 0
        self.map = MAPS[self.mapid]



        self.map, self.startPos, self.lowest = map_to_auto(self.map)
        self.player = Player((self.startPos[0], self.startPos[1]))


        self.lowest = generate_map(self.tiles, self.map, self.enemies, self)

    def draw(self):
        self.screen.blit(self.player.image, self.player.rect)
        self.tiles.draw(self.screen)
        self.screen.blit(self.pshield.image, self.pshield.rect)



    def update(self):
        run = True
        while run:
            #print(self.pshield.rad)
            if len(self.enemies) <= 0:
                try:
                    self.mapid += 1
                    self.map = MAPS[self.mapid]
                except:
                    print('you win')
                    pygame.quit()
                    sys.exit()
                self.tiles.empty()
                self.enemies.empty()
                self.map, self.startPos, self.lowest = map_to_auto(self.map)
                self.player.rect.y = self.startPos[1] - 800
                self.player.rect.x = self.startPos[0]
                self.lowest = generate_map(self.tiles, self.map, self.enemies, self)


            #print(self.player.rect.y)
            if self.lowest.rect.y < 0:
                self.player.rect.y = self.startPos[1] - 800
                self.player.rect.x = self.startPos[0]
                self.tiles.empty()
                self.enemies.empty()
                self.lowest = generate_map(self.tiles, self.map, self.enemies, self)

            self.clock.tick(60)
            self.screen.fill((66, 155, 245))
            self.draw()
            for e in self.enemies:
                e.shoot(self.player, self.screen, self.pshield, self.tiles, self.enemies, self.gloabalBullets, self)
                pass


            self.pshield = self.player.move(self.pshield, self.tiles, self.screen)
            self.pshield.look_at_m()

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    run = False
                    break

            pygame.display.flip()

        pygame.quit()
        sys.exit()

g  = Game()

g.update()

