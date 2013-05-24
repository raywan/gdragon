import pygame
from sprites import *

class MainMap(object):
    def __init__(self, parent, x, y):
        self.game = parent
        self.tile = Tile()
        self.map = pygame.Surface((320,320))
        self.rect = self.map.get_rect()
        self.solid_list = pygame.sprite.Group()

        self.tile_layer_1 = []
        for i in range (100):
            self.tile_layer_1.append(1)

        self.tile_layer_2 = []
        for j in range(100):
            self.tile_layer_2.append(0)
        self.tile_layer_2[15] = 2
        self.tile_layer_2[18] = 2

        self.load_tiles()
        self.render_tiles(self.tile_layer_1,(x,y))
        self.render_tiles(self.tile_layer_2,(x,y))
    def load_tiles(self):
        self.grass = self.tile.grass.tile
        self.null = self.tile.null.tile
    def render_tiles(self, tile_array, map_pos):
        tile_column = 1
        tile_row = 1
        for i in range(len(tile_array)):
            if tile_array[i] == 0:
                None
            elif tile_array[i] == 1:
                self.map.blit(self.grass, (32*(tile_column - 1), 32*(tile_row - 1)))
            elif tile_array[i] == 2:
                x = 32*(tile_column - 1)
                y = 32*(tile_row - 1)
                self.render_solids("rock", x, y)
            else:
                self.map.blit(self.null.tile, (32*(tile_column - 1), 32*(tile_row - 1)))
            tile_column += 1
        
            if tile_column > (self.map.get_size()[1]//32):
                tile_column = 1
                tile_row += 1
                    
        # TESTING SCALING
        # self.map_surf = pygame.transform.scale(self.map_surf, (self.map_surf.get_size()[0] *
        #     self.game.SCALE, self.map_surf.get_size()[1] * self.game.SCALE))
    def render_solids(self, solid, x, y):
        if solid == "rock":
            self.rock = RockTile(x,y)
            self.solid_list.add(self.rock)
        else:
            print "None" 
    def get_solids(self):
        return self.solid_list
    def render(self):
        self.game.screen.blit(self.map, self.rect)
