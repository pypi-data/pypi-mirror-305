import pygame as pg
import math

pg.init()
class Math:
    def vector(posx, posy, targetx, targety, speed):
        distance = [targetx - posx, targety - posy]
        norm = math.sqrt(distance[0] ** 2 + distance[1] ** 2)
        dx = distance[0] / norm
        dy = distance[1] / norm
        vector = [dx * speed, dy * speed]
        return vector

class entity:
    class Player:
        def __init__(self, posx, posy, size):
            self.x = posx
            self.y = posy
            self.rect = pg.Rect((self.x, self.y), size)

        def controls(self, posx, posy, speed):
            self.keys = pg.key.get_pressed()
            if self.keys[pg.K_d]:
                posx += 1 * speed
            if self.keys[pg.K_a]:
                posx -= 1 * speed
            if self.keys[pg.K_w]:
                posy -= 1 * speed
            if self.keys[pg.K_s]:
                posy += 1 * speed
            return posx, posy

        def dash(self, posx, posy, length):
            self.keys = pg.key.get_pressed()
            if self.keys[pg.K_d]:
                posx += length
            if self.keys[pg.K_a]:
                posx -= length
            if self.keys[pg.K_s]:
                posy += length
            if self.keys[pg.K_w]:
                posy -= length
            return posx, posy

    class Enemy:
        def __init__(self, posx, posy, size):
            self.x = posx
            self.y = posy
            self.rect = pg.Rect((self.x, self.y), size)

        def follow(self, posx, posy, targetx, targety, speed):
            self.dx = targetx - posx
            self.dy = targety - posy
            self.dist = (self.dx ** 2 + self.dy ** 2) ** 0.5
            if self.dist > 0:
                self.dx /= self.dist
                self.dy /= self.dist
                posx += self.dx * speed
                posy += self.dy * speed
            self.pos = [posx, posy]
            return self.pos
        
    def update(entity):
        entity = entity
        entity.rect.x = entity.x
        entity.rect.y = entity.y

class Sprite:
    def getImage(path, scale=1, colorkey='black'):
        image = pg.transform.scale_by(pg.image.load(path), scale)
        image.set_colorkey(colorkey)
        return image

    def getImageFromSpriteSheet(spritesheet, size, picNum=0):
        size1, size2 = size
        surface = pg.surface.Surface(size)
        surface.blit(spritesheet, (0, 0), (picNum * size1, 0, size1, size2))
        return surface
        
class Bullet:
    def __init__(self, posx, posy, size):
        self.x, self.y = posx, posy
        self.rect = pg.Rect((self.x, self.y), size)

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y