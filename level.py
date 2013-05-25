import pygame
from sprites import *

class MainMap(object):
    def __init__(self, parent):
        self.game = parent
        self.tile = Tile()
        self.solid_list = pygame.sprite.Group()

        #ocean layer
        self.outer_water_map = pygame.Surface((1024,1024))
        self.outer_water_map_rect = self.outer_water_map.get_rect()
        self.outer_water_map_rect.x = -208
        self.outer_water_map_rect.y = -208

        #main land layer
        self.land_map = pygame.Surface((320,320))
        self.rect = self.land_map.get_rect()

        #DEBUG TILE ARRAYS
        self.outer_water_layer = []
        for w in range(1024):
            self.outer_water_layer.append(1)

        self.tile_layer_1 = []
        for i in range (100):
            self.tile_layer_1.append(2)

        self.tile_layer_2 = []
        for j in range(100):
            self.tile_layer_2.append(0)
        self.tile_layer_2[15] = 3
        self.tile_layer_2[17] = 3

        self.map_border = []
        for k in range(90):
            self.map_border.append(0)
        for k in range(10):
            self.map_border.append(4)

        self.load_tiles()

        #TEMP LAYER RENDERING
        self.render_tiles(self.outer_water_map, self.outer_water_layer)
        self.render_tiles(self.land_map, self.tile_layer_1)
        self.render_tiles(self.land_map, self.tile_layer_2)
        self.render_tiles(self.land_map, self.map_border)

    def load_tiles(self):
        self.grass = self.tile.grass.tile
        self.outer_water = self.tile.outer_water.tile
        self.null = self.tile.null.tile 
    def render_tiles(self, surf, tile_array):
        tile_column = 1
        tile_row = 1
        for i in range(len(tile_array)):
            if tile_array[i] == 0:
                None
            elif tile_array[i] == 1:
                surf.blit(self.outer_water, (32*(tile_column - 1), 32*(tile_row - 1)))
            elif tile_array[i] == 2:
                surf.blit(self.grass, (32*(tile_column - 1), 32*(tile_row - 1)))
            elif tile_array[i] == 3:
                x = 32*(tile_column - 1)
                y = 32*(tile_row - 1)
                self.render_solids("rock", x, y)
            elif tile_array[i] == 4:
                x = 32*(tile_column - 1)
                y = 32*(tile_row - 1)
                self.render_solids("beach_edge", x, y)
            else:
                surf.blit(self.null, (32*(tile_column - 1), 32*(tile_row - 1)))
            tile_column += 1
        
            if tile_column > (surf.get_size()[1]//32):
                tile_column = 1
                tile_row += 1
                    
        # TESTING SCALING
        # self.map_surf = pygame.transform.scale(self.map_surf, (self.map_surf.get_size()[0] *
        #     self.game.SCALE, self.map_surf.get_size()[1] * self.game.SCALE))
    def render_solids(self, solid, x, y):
        if solid == "rock":
            self.rock = RockTile(x,y)
            self.solid_list.add(self.rock)
        elif solid == "beach_edge":
            self.beach_edge = BeachEdge(x,y)
            self.solid_list.add(self.beach_edge)
        else:
            print "None" 
    def get_solids(self):
        return self.solid_list
    def render(self):
        self.game.screen.blit(self.outer_water_map, self.outer_water_map_rect) 
        self.game.screen.blit(self.land_map, self.rect)

class CaveMap(object):
    def __init__(self, parent):
        self.game = parent
        self.tile = Tile()
        self.solid_list = pygame.sprite.Group()

        self.cave_floor_map = pygame.Surface((640,320))
        self.rect = self.cave_floor_map.get_rect()

        self.tile_array = [
                "00001111111110000001",
                "00001111111110000001",
                "00001111111110000001",
                "00001111111111111111",
                "00001111111111111111",
                "00001111111110000000",
                "00001111111110000000",
                "00000001111110000000",
                "00000001111110000000",
                "00000001111110000000",]
        self.load_tiles()

        self.render_tiles(self.cave_floor_map, self.tile_array)

    def load_tiles(self):
        self.cave_floor = self.tile.cave_floor.tile
        self.null = self.tile.null.tile 
    def render_tiles(self, surf, tile_array):
        tile_column = 1
        tile_row = 1

        for row in tile_array:
            for col in row:
                if col == '0':
                    None
                elif col == '1':
                    surf.blit(self.cave_floor, (32*(tile_column - 1), 32*(tile_row - 1)))
                elif col == '4':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("beach_edge", x, y)
                else:
                    surf.blit(self.null, (32*(tile_column - 1), 32*(tile_row - 1)))
                tile_column += 1
        
            if tile_column > (surf.get_size()[1]//32):
                tile_column = 1
                tile_row += 1
        
        # TESTING SCALING
        # self.map_surf = pygame.transform.scale(self.map_surf, (self.map_surf.get_size()[0] *
        #     self.game.SCALE, self.map_surf.get_size()[1] * self.game.SCALE))
    def render_solids(self, solid, x, y):
        if solid == "rock":
            self.rock = RockTile(x,y)
            self.solid_list.add(self.rock)
        elif solid == "beach_edge":
            self.beach_edge = BeachEdge(x,y)
            self.solid_list.add(self.beach_edge)
        else:
            print "None" 
    def get_solids(self):
        return self.solid_list
    def render(self):
        self.game.screen.blit(self.cave_floor_map, self.rect)
