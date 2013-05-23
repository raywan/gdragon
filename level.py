import pygame
from sprites import *

class Level(object):
    def __init__(self):
        pass
    def get_tiles(self):
        pass
        
class MainMap(Level):
    def __init__(self, parent, x, y):
        Level.__init__(self)
        self.game = parent
        self.tile = Tile()
        self.map = pygame.Surface((320,320))
        self.rect = self.map.get_rect()
        self.tile_array = []
        self.solid_list = pygame.sprite.Group()
        for i in range (100):
            self.tile_array.append(0)
        self.tile_array[14] = 2
        self.tile_array[17] = 2
        self.load_tiles()
        self.render_tiles((x,y))
    def load_tiles(self):
        self.grass = self.tile.grass.tile
        self.rock = self.tile.rock.tile
        self.null = self.tile.null.tile
    def render_tiles(self, map_pos):
        tile_column = 1
        tile_row = 1
        for i in range(len(self.tile_array)):
            if self.tile_array[i] == 0:
                self.map.blit(self.grass, (32*(tile_column - 1), 32*(tile_row - 1)))
            elif self.tile_array[i] == 2:
                rock = self.tile.new_rock()
                self.map.blit(rock.tile,(32*(tile_column - 1), 32*(tile_row - 1)))
                self.solid_list.add(rock)
            
            else:
                self.map.blit(self.null.tile, (32*(tile_column - 1), 32*(tile_row - 1)))
            tile_column += 1
        
            if tile_column > (self.map.get_size()[1]//32):
                tile_column = 1
                tile_row += 1
                    
        # TESTING SCALING
        # self.map_surf = pygame.transform.scale(self.map_surf, (self.map_surf.get_size()[0] *
        #     self.game.SCALE, self.map_surf.get_size()[1] * self.game.SCALE))
    def render(self):
        self.game.screen.blit(self.map, self.rect)
