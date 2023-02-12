from enemy import Enemy
from tile import Tile, ImageTile

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
                t = ImageTile((x * 50, y * 50), group, 'grass.png')
                lowest = t


    return lowest