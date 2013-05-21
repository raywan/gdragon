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

class Player(pygame.sprite.Sprite):
    d_x = 0
    d_y = 0
    def __init__(self, parent, init_pos):
        self.game = parent
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = SpriteSheet("test_spritesheet.png")
        self.img = self.spritesheet.load((32,0,32,32),(255,0,255))
        #TESTING SCALING
        # self.img = pygame.transform.scale(self.img, (32 * self.game.SCALE, 32 * self.game.SCALE))
        #
        self.rect = self.img.get_rect()
        self.rect.x = init_pos[0]
        self.rect.y = init_pos[1]
    def move(self, x, y):
        self.d_x += x
        self.d_y += y
    def update(self):
        self.old_x = self.rect.x
        self.new_x = self.old_x + self.d_x
        self.rect.x = self.new_x

        self.old_y = self.rect.y
        self.new_y = self.old_y + self.d_y
        self.rect.y = self.new_y

    def render(self):
        self.game.screen.blit(self.img, self.rect)

class NullTile(pygame.sprite.Sprite):
    def __init__(self, parent):
        self.parent = parent
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = SpriteSheet("test_spritesheet.png")
        self.tile = self.spritesheet.load((0,0,32,32),(255,0,255))

class GrassTile(pygame.sprite.Sprite):
    def __init__(self, parent):
        self.parent = parent
        pygame.sprite.Sprite.__init__(self)
        self.spritesheet = SpriteSheet("test_spritesheet.png")
        self.tile = self.spritesheet.load((64,0,32,32),(255,0,255))
        # self.tile = pygame.transform.scale(self.tile, (32 * self.parent.game.SCALE, 32 *
        #     self.parent.game.SCALE))

class Map(object):
    def __init__(self, parent):
        self.game = parent
        self.grass = GrassTile(self)
        self.null = NullTile(self)
        self.map_surf = pygame.Surface((320,320))
        #DEBUG TILE ARRAY
        self.tile_array = [1]
        for x in range(99):
            self.tile_array.append(0)

    def render_tiles(self):
        tile_column = 1
        tile_row = 1
        for i in range(len(self.tile_array)):
            if self.tile_array[i] == 0:
                self.map_surf.blit(self.grass.tile, (32*(tile_column - 1), 32*(tile_row - 1)))
            else:
                self.map_surf.blit(self.null.tile, (32*(tile_column - 1), 32*(tile_row - 1)))
            tile_column += 1
        
            if tile_column > (self.map_surf.get_size()[1]//32):
                tile_column = 1
                tile_row += 1
            
        # TESTING SCALING
        # self.map_surf = pygame.transform.scale(self.map_surf, (self.map_surf.get_size()[0] *
        #     self.game.SCALE, self.map_surf.get_size()[1] * self.game.SCALE))
        
    def render_map(self):
        self.game.screen.blit(self.map_surf, (0,0))


