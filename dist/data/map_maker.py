import sys

import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 750))

pygame.mouse.set_visible(False)

outmap = [[0 for i in range(int(1000 / 50))] for i in range(int((750 * 5) / 50))]

print(outmap)

mpos = pygame.mouse.get_pos()

x = 0
y = 0

rect = pygame.Rect(x, y, 50, 50, )


def myround(x, base=50):
    return base * round(x / base)


class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)


tiles = pygame.sprite.Group()

mapx = x
mapy = y

tile_id = 0

colors = {
    0: 'black',
    1: 'green',
    2: 'orange'
}

yoff = 0

while True:
    mpos = pygame.mouse.get_pos()
    screen.fill('black')

    rect = pygame.Rect(x, y - yoff, 50, 50, )

    tiles.draw(screen)

    pygame.draw.rect(screen, 'red', rect, 3)

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            outmap[mapy][mapx] = tile_id
            print(f'{y}:{x}')
            t = Tile((x, y-yoff), colors[tile_id])
            tiles.add(t)

        tile_id %= len(colors)

        x = myround(mpos[0])
        y = myround(mpos[1]) + yoff
        mapx = int(x / 50)
        mapy = int(y / 50)

        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_e:
                print(outmap)
            if ev.key == pygame.K_w:
                tile_id += 1
            if ev.key == pygame.K_s:
                tile_id -= 1
            if ev.key == pygame.K_DOWN:
                for tile in tiles:
                    tile.rect.y -= 750
                yoff += 750
                mapy += 1

    pygame.display.flip()
