###############
#objects for the Tile() class


##########################################################################
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

class FoodStandBottomTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/FoodStands.png")
        self.image = self.spritesheet.load((0,96,32,32), (255,0,255))
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
###################
class LargeTableSeven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((0,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableEight (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((32,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableNine (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((64,64,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
##################
class LargeTableTen (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((0,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableEleven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/LargeTable.png")
        self.image = self.spritesheet.load((32,96,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class LargeTableTwelve (Entity) :
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
###################################################################

class RandomBoatOne (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((0,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class RandomBoatTwo (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((32,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class RandomBoatThree (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((64,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class RandomBoatFour (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((96,0,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
#######################
class RandomBoatFive (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((0,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class RandomBoatSix (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((32,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class RandomBoatSeven (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((64,32,32,32), (255,0,255))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class RandomBoatEight (Entity) :
    def __init__(self, x, y) :
        Entity.__init__(self)
        self.spritesheet = SpriteSheet("res/RandomBoat.png")
        self.image = self.spritesheet.load((96,32,32,32), (255,0,255))
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
