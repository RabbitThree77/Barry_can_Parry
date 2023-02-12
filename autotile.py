import pygame

def map_to_auto(map):
    global map2
    l = []
    p = [0, 0]
    for x,row in enumerate(map):
        for y in range(len(row)):
            l.append(map[x][y])
            map2 = list(map)
            if map[x][y] == 4:
                p = [y*50, x*50]
                print(x)
                print(y)
            try:
                if map2[x-1][y] == 0 or map2[x-1][y] == 2 or map2[x-1][y] == 4:
                    if map2[x][y] == 1:
                        map2[x][y] = 3
                if map2[x][y] == 3 and map2[x+1][y] == 0:
                    map2[x][y] = 3
                if map2[x][y] == 3 and map2[x-1][y] == 0:# and map2[x+1][y] == 3:
                    map2[x][y] = 3

                # if map[x+1][y] == 0 and map[x][y] == 1:
                #     map2[x][y] = 4
                # if map[x+1][y] == 0 and map[x][y] == 3:
                #     map2[x][y] = 5

            except: pass
            lowest = [y*50, x*50]

    return [map2, p, lowest]
