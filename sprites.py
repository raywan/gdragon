import pygame
# http://www.devshed.com/c/a/Python/PyGame-for-Game-Development-Sprite-Groups-and-Collision-Detection/

class SpriteSheet(object): 
    #http://www.pygame.org/wiki/Spritesheet
    def __init__(self, path):
        try:
            self.spritesheet = pygame.image.load(path).convert()
        except pygame.error, message:
            print "Unable to load spritesheet image:", path

    def load(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.spritesheet, (0,0), rect)
        if colorkey != None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

class Entity(pygame.sprite.Sprite):
    def __init__(self):
       pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    d_x = 0
    d_y = 0
    def __init__(self, parent, init_pos):
        self.game = parent
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("test_spritesheet.png")
        self.img = self.spritesheet.load((32,0,32,32),(255,0,255))
        self.mask = pygame.mask.from_surface(self.img)
        #TESTING SCALING
        # self.img = pygame.transform.scale(self.img, (32 * self.game.SCALE, 32 * self.game.SCALE))
        #
        self.rect = self.img.get_rect()
        self.rect.x = init_pos[0]
        self.rect.y = init_pos[1]
    def move(self, x, y):
        self.d_x += x
        self.d_y += y

    def update(self, solids):
        self.old_x = self.rect.x
        self.new_x = self.old_x + self.d_x
        self.rect.x = self.new_x

        if self.collide(solids):
            self.rect.x = self.old_x

        self.old_y = self.rect.y
        self.new_y = self.old_y + self.d_y
        self.rect.y = self.new_y

        if self.collide(solids):
            self.rect.y = self.old_y

    def render(self):
        self.game.screen.blit(self.img, self.rect)

    def collide(self,solids):
        # http://rene.f0o.com/~rene/stuff/pyzine/html_out/pixel_perfect_collision/index.html
        self.solids = solids
        collide = pygame.sprite.spritecollide(self, solids, False, pygame.sprite.collide_mask)
        return collide

class Tile(object):
    def __init__(self):
        self.grass = GrassTile()
        # self.rock = RockTile()
        self.null = NullTile()

class NullTile(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("test_spritesheet.png")
        self.tile = self.spritesheet.load((0,0,32,32),(255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class GrassTile(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("test_spritesheet.png")
        self.tile = self.spritesheet.load((64,0,32,32),(255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()
        # self.rect.x = x
        # self.rect.y = y

        # self.tile = pygame.transform.scale(self.tile, (32 * self.parent.game.SCALE, 32 *
        #     self.parent.game.SCALE))

class RockTile(Entity):
    def __init__(self, x ,y):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("test_spritesheet.png")
        self.image = self.spritesheet.load((0,32,32,32),(255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

