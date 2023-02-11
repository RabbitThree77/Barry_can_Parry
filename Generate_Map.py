from enemy import Enemy
from tile import Tile, ImageTile

def generate_map(group, map, engroup, game):
    for y,row in enumerate(map):
        for x,tile in enumerate(row):
            if tile == 1:
                Tile((x*50,y*50), group)
            elif tile == 2:
                Enemy((x*50,y*50), engroup, group)
            elif tile == 3:
                ImageTile((x * 50, y * 50), group, 'grass.png')
            elif tile == 4:
                ImageTile((x * 50, y * 50), group, 'bottom.png')
            elif tile == 5:
                ImageTile((x * 50, y * 50), group, 'bottom_grass.png')
            elif tile == 6:
                ImageTile((x * 50, y * 50), group, 'grass_side_left.png')