import pygame
# http://www.devshed.com/c/a/Python/PyGame-for-Game-Development-Sprite-Groups-and-Collision-Detection/

class SpriteSheet(object): 
    #http://www.pygame.org/wiki/SpriteSheet
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
        self.parent = parent
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/characters.png")
        self.img = self.spritesheet.load((224,0,32,32),(255,0,255))
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

    def update(self, solids, entrance):
        self.old_x = self.rect.x
        self.new_x = self.old_x + self.d_x
        self.rect.x = self.new_x
        
        if self.collide_entrance(entrance):
            self.parent.current_map = self.parent.change_map("cave")

        if self.collide(solids):
            self.rect.x = self.old_x

        self.old_y = self.rect.y
        self.new_y = self.old_y + self.d_y
        self.rect.y = self.new_y

        if self.collide(solids):
            self.rect.y = self.old_y

    def render(self):
        self.parent.game.screen.blit(self.img, self.rect)

    def collide(self,solids):
        # http://rene.f0o.com/~rene/stuff/pyzine/html_out/pixel_perfect_collision/index.html
        collide = pygame.sprite.spritecollide(self, solids, False, pygame.sprite.collide_mask)
        return collide

    def collide_entrance(self, entrance):
        entrance_collide = pygame.sprite.spritecollide(self, entrance, False,
                pygame.sprite.collide_mask)
        return entrance_collide
    def is_moving(self):
        if self.d_x != 0 or self.d_y != 0:
            return True
        else:
            return False
class Tile(object) :
    def __init__(self) :
        self.null = NullTile()
        self.outer_water = OuterWater()
        self.main_grass = MainGrass()
        self.grass_weed = GrassWeed()
        self.cave_floor = CaveFloor()
        ###
        self.cliff_grass_top_left = cliff_grassTopLeft()
        self.cliff_grass_middle_top = cliff_grassMiddleTop()
        self.cliff_grass_right_top = cliff_grassRightTop()
        
        self.cliff_grass_left_center = cliff_grassLeftCenter()
        self.cliff_grass_right_center = cliff_grassRightCenter()
        
        self.cliff_dark_grass_left_top = CliffDarkGrassLeftTop()
        self.cliff_dark_grass_middle_top = CliffDarkGrassMiddleTop()
        self.cliff_dark_grass_right_top = CliffDarkGrassRightTop()

        self.cliff_dark_grass_left_center = CliffDarkGrassLeftCenter()
        self.cliff_dark_grass_middle_center = CliffDarkGrassMiddleCenter()
        self.cliff_dark_grass_right_center = CliffDarkGrassRightCenter()

        self.cliff_dark_grass_left_bottom = CliffDarkGrassLeftBottom()
        self.cliff_dark_grass_middle_bottom = CliffDarkGrassMiddleBottom()
        self.cliff_dark_grass_right_bottom = CliffDarkGrassRightBottom()

        self.cliff_dark_grass_column_top = CliffDarkGrassColumnTop()
        self.cliff_dark_grass_column_middle = CliffDarkGrassColumnMiddle()
        self.cliff_dark_grass_column_bottom = CliffDarkGrassColumnBottom()

        self.cliff_dark_grass_box = CliffDarkGrassBox()

        self.cliff_dark_grass_bottom_row_left = CliffDarkGrassBottomRowLeft()
        self.cliff_dark_grass_bottom_row_middle = CliffDarkGrassBottomRowMiddle()
        self.cliff_dark_grass_bottom_row_right = CliffDarkGrassBottomRowRight()
        ###
        
class NullTile(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/test_spritesheet.png")
        self.tile = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class OuterWater(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/test_spritesheet.png")
        self.tile = self.spritesheet.load((96,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()
#########################################################################
#from file Grass2.png
class MainGrass (Entity) :
    def __init__(self):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/grass2.png")
        self.tile = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class GrassWeed (Entity) :
    def __init__(self):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/grass2.png")
        self.tile = self.spritesheet.load((160,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CaveFloor (Entity) :
    def __init__(self):
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/grass2.png")
        self.tile = self.spritesheet.load((128,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()
 #########################################################################       
#from Cliff.png, first 96x96 square
        #top row
class cliff_grassTopLeft (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class cliff_grassMiddleTop (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class cliff_grassRightTop (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((64,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()
        
        #middle row
class cliff_grassLeftCenter (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class cliff_grassRightCenter (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((64,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

        #bottom row
class CliffSideSmallLeft (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((0,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CliffSideSmallCenter (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((32,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class CliffSideSmallRight (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((64,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


#from Cliff.png, second 96x96 square
        #top row
class CliffSideLargeLeftTop (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((96,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CliffSideLargeMiddleTop (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((128,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CliffSideLargeRightTop (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((160,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #middle row
class CliffSideLargeLeftCenter (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((96,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CliffSideLargeMiddleCenter (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((128,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CliffSideLargeRightCenter (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((160,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #bottow row
class CliffSideLargeLeftBottom (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((96,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CliffSideLargeMiddleBottom (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((128,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class CliffSideLargeRightBottom (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.image = self.spritesheet.load((160,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# from Cliff.png, third 96x96 box
        #top row
class CliffDarkGrassLeftTop (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((192,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassMiddleTop (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((224,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassRightTop (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((256,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

        #middle row
class CliffDarkGrassLeftCenter (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((192,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassMiddleCenter (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((224,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()


class CliffDarkGrassRightCenter (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((256,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

        #bottom row
class CliffDarkGrassLeftBottom (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((192,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassMiddleBottom (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((224,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassRightBottom (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((256,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

# from Cliff.png, third 128x96 box
        #first column
class CliffDarkGrassColumnTop (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((288,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassColumnMiddle (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((288,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassColumnBottom (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((288,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

        #Middle Box
class CliffDarkGrassBox (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((320,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

        #Bottom row
class CliffDarkGrassBottomRowLeft (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((320,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassBottomRowMiddle (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((352,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()

class CliffDarkGrassBottomRowRight (Entity) :
    def __init__(self) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/cliff_grass.png")
        self.tile = self.spritesheet.load((384,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.tile)
        self.rect = self.tile.get_rect()
#############################################################################

#1x1 box for colliding
class Top(Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/1x1pixelbox.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Bottom(Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/1x1pixelbox.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Left(Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/1x1pixelbox.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Right(Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/1x1pixelbox.png")
        self.image = self.spritesheet.load((32,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

###################################################################
    #from CaveEntrance.png

class CaveEntrance (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/CaveEntrance.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

###################################################################
    #from CaveWalls.png

class CaveWalls (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/CaveWalls.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

####################################################################
class BerryBush (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/berrybush.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
###########################################################################
class Bush (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/bush.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
############################################################################
class BigTreeOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeThree (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((64,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeFour (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((96,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
################

class BigTreeFive (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeSix (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((32,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class BigTreeSeven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((64,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeEight (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((96,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
##########################
class BigTreeNine (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((0,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeTen (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((32,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeEleven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((64,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeTwelve (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((96,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
########################
class BigTreeThirteen (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((0,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeFourteen (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((32,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeFifteen (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((64,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class BigTreeSixteen (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/big_tree.png")
        self.image = self.spritesheet.load((96,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
###########################################################################

class FoodStandOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandThree (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((64,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandFour (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((96,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandBottomOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandFive (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((0,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandSix (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((32,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandSeven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((64,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class FoodStandEight (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((96,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

##############################################################################
        
class TentFoodStandOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeFoodStand.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class TentFoodStandTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeFoodStand.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class TentFoodStandThree (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeFoodStand.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class TentFoodStandFour (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeFoodStand.png")
        self.image = self.spritesheet.load((32,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class TentFoodStandFive (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeFoodStand.png")
        self.image = self.spritesheet.load((0,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class TentFoodStandSix (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeFoodStand.png")
        self.image = self.spritesheet.load((32,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#####################################################################

class LargeTableOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableThree (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((64,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
###################
class LargeTableFour (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableFive (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((32,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableSix (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((64,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
##################
class LargeTableSeven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((0,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableEight (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((32,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableNine (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((64,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#######################################################################

class SmallTableOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/SmallTable.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class SmallTableTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/SmallTable.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
######################################################################

class LargeLogsOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeLogs.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeLogsTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeLogs.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeLogsThree (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeLogs.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeLogsFour (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeLogs.png")
        self.image = self.spritesheet.load((32,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
############################################################################

class ObjectsOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ObjectsTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ObjectsThree (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((64,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#######################
class ObjectsFour (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ObjectsFive (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((32,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ObjectsSix (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((64,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
######################
class ObjectsSeven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((0,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ObjectsEight (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((32,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class ObjectsNine (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/32x32Objects.png")
        self.image = self.spritesheet.load((64,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#########################################################################








        
