import pygame
#from enemy import Enemy


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, group, col = '#AB5236'):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(col)
        self.rect = self.image.get_rect(topleft = pos)
        group.add(self)

class ImageTile(pygame.sprite.Sprite):
    def __init__(self, pos, group, src, ):
        super().__init__()
        self.image = pygame.image.load(str(src))
        self.image = pygame.transform.scale(self.image, (50,50))
        #self.image.fill(col)
        self.rect = self.image.get_rect(topleft = pos)
        group.add(self)

