import pygame, math

class Player:
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill('dark green')
        self.rect = self.image.get_rect(center = pos)
        self.speed = 5

        self.jump = False
        self.jumpvel = 15
        self.onground = False
        self.doublejump = False

    def move(self, shield, tiles, screen):
        keys = pygame.key.get_pressed()




        movement = [0,0]

        if keys[pygame.K_a]:
            movement[0] = -self.speed
        elif keys[pygame.K_d]:
            movement[0] = self.speed


        if keys[pygame.K_w] and not self.jump and self.onground:

            self.jump = True
            self.onground = False

        if self.jump:
            movement[1] -= self.jumpvel + self.speed #to negate gravity
            self.jumpvel -= 1
            if self.jumpvel < -10:
                self.jump = False
                self.jumpvel = 15


        elif keys[pygame.K_s]:
            movement[1] = self.speed

        if not self.jump:
            movement[1] += 10


        if self.rect.x < 450:
            for t in tiles:
                t.rect.x += self.speed
            self.rect.x += self.speed
        elif self.rect.x > 550:
            for t in tiles:
                t.rect.x -= self.speed
            self.rect.x -= self.speed

        if self.rect.y > 400:
            for t in tiles:
                t.rect.y -= 10
            self.rect.y -= 10
        if self.rect.y < 300:
            for t in tiles:
                t.rect.y += self.speed
            self.rect.y += self.speed


        self.rect[0] += movement[0]
        for t in tiles:
            if t.rect.colliderect(self.rect):
                if movement[0] > 0:

                    self.rect.right = t.rect.left
                if movement[0] < 0:

                    self.rect.left = t.rect.right




        self.rect[1] += movement[1]
        for t in tiles:
            if t.rect.colliderect(self.rect):
                if movement[1] > 0:
                    self.onground = True
                    self.rect.bottom = t.rect.top
                if movement[1] < 0:
                    if self.jump:
                        self.jump = False
                        self.jumpvel = 15
                    self.rect.top = t.rect.bottom






        shield.pos = self.rect.center
        #shield.rect = pygame.Rect(shield.rect[0], shield.rect[1], shield.rect[2], shield.rect[3])

        return shield


class Shield:
    def __init__(self):
        self.image = pygame.Surface((75,15), pygame.SRCALPHA)
        self.image.fill('dark grey')
        self.rect = self.image.get_rect(center=(500, 310))
        self.pos = list(self.rect.center)
        self.oimg = self.image
        self.offset = pygame.math.Vector2(0, 30)
        self.rad = 0

    def look_at_m(self):
        mpos = pygame.mouse.get_pos()
        rad = math.atan2(mpos[1]-self.pos[1], mpos[0]-self.pos[0])
        self.rad = rad
        rad = round(rad * 180/math.pi)


        offset_rotated = self.offset.rotate(rad+90)

        self.image = pygame.transform.rotate(self.oimg, -rad-90)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos - offset_rotated)
        #self.pos = self.rect.center