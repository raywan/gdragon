import pygame
from sprites import *

class MainMap(object):
    def __init__(self, parent):
        self.game = parent
        self.tile = Tile()
        self.all_sprites =  pygame.sprite.Group()
        self.solid_list = pygame.sprite.Group()
        self.entrance_list = pygame.sprite.Group()

        #main land layer
        self.land_map = pygame.Surface((320,320))
        self.rect = self.land_map.get_rect()

        #DEBUG TILE ARRAYS
        self.land_layer = []
        for w in range(32):
            self.land_layer.append("1"*32)

        self.tile_layer_1 = [
                "1111111111",
                "1111111111",
                "1111111111",
                "1111111111",
                "1111111111",
                "1111111111",
                "1111111111",
                "1111111111",
                "1111111111",
                "1111111111"]

        self.tile_layer_2 = [
                "2333333334",
                "5111111116",
                "5111111116",
                "accgcccccb",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000"]

        self.map_border = [
                "f00000000d",
                "f00000000d",
                "f00000000d",
                "f00000000d",
                "f00000000d",
                "f00000000d",
                "f00000000d",
                "f00000000d",
                "f00000000d",
                "feeeeeeeed"]
        self.map_border_2 = [
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "0000000000",
                "e00000000e"]

        self.load_tiles()

        #TEMP LAYER RENDERING
        self.render_tiles(self.land_map, self.land_layer)
        self.render_tiles(self.land_map, self.tile_layer_1)
        self.render_tiles(self.land_map, self.tile_layer_2)
        self.render_tiles(self.land_map, self.map_border)
        self.render_tiles(self.land_map, self.map_border_2)

    def load_tiles(self):
        self.main_grass = self.tile.main_grass.tile
        self.cliff_grass_top_left = self.tile.cliff_grass_top_left.tile
        self.cliff_grass_middle_top = self.tile.cliff_grass_middle_top.tile
        self.cliff_grass_right_top = self.tile.cliff_grass_right_top.tile
        self.cliff_grass_left_center = self.tile.cliff_grass_left_center.tile
        self.cliff_grass_right_center = self.tile.cliff_grass_right_center.tile
        self.null = self.tile.null.tile 
    def render_tiles(self, surf, tile_array):
        tile_column = 1
        tile_row = 1
        for row in tile_array:
            for col in row:
                if col == '0':
                    None
                elif col == '1':
                    surf.blit(self.main_grass, (32*(tile_column - 1), 32*(tile_row - 1)))
                elif col == '2':
                    surf.blit(self.cliff_grass_top_left, (32*(tile_column - 1), 32*(tile_row - 1)))
                elif col == '3':
                    surf.blit(self.cliff_grass_middle_top, (32*(tile_column - 1), 32*(tile_row - 1)))
                elif col == '4':
                    surf.blit(self.cliff_grass_right_top, (32*(tile_column - 1), 32*(tile_row - 1)))
                elif col == '5':
                    surf.blit(self.cliff_grass_left_center, (32*(tile_column - 1), 32*(tile_row - 1)))
                elif col == '6':
                    surf.blit(self.cliff_grass_right_center, (32*(tile_column - 1), 32*(tile_row - 1)))
                elif col == 'a':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("SmallCliffLeft", x, y)
                elif col == 'b':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("SmallCliffRight", x, y)
                elif col == 'c':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("SmallCliffCenter", x, y)
                elif col == 'd':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("RightBorder", x, y)
                elif col == 'e':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BottomBorder", x, y)
                elif col == 'f':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("LeftBorder", x, y)
                elif col == 'g':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_column - 1)
                    self.render_enterable("CaveEntrance", x, y)
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
        if solid == "SmallCliffLeft":
            self.cliff_side_small_left = CliffSideSmallLeft(x,y)
            self.all_sprites.add(self.cliff_side_small_left)
            self.solid_list.add(self.cliff_side_small_left)
        elif solid == "SmallCliffRight":
            self.cliff_side_small_right = CliffSideSmallRight(x,y)
            self.all_sprites.add(self.cliff_side_small_right)
            self.solid_list.add(self.cliff_side_small_right)
        elif solid == "SmallCliffCenter":
            self.cliff_side_small_center = CliffSideSmallCenter(x,y)
            self.all_sprites.add(self.cliff_side_small_center)
            self.solid_list.add(self.cliff_side_small_center)
        elif solid == "LeftBorder":
            self.left = Left(x,y)
            self.all_sprites.add(self.left)
            self.solid_list.add(self.left)
        elif solid == "RightBorder":
            self.right = Right(x,y)
            self.all_sprites.add(self.right)
            self.solid_list.add(self.right)
        elif solid == "BottomBorder":
            self.bottom = Bottom(x,y)
            self.all_sprites.add(self.bottom)
            self.solid_list.add(self.bottom)
        elif solid == "TopBorder":
            self.top = Top(x,y)
            self.all_sprite.add(self.top)
            self.solid_list.add(self.top)
        else:
            print "None" 
    def render_enterable(self, enterable, x, y):
        if enterable == "CaveEntrance":
            self.cave_entrance = CaveEntrance(x,y)
            self.all_sprites.add(self.cave_entrance)
            self.entrance_list.add(self.cave_entrance)
    def get_all_sprites(self):
        return self.all_sprites
    def get_solids(self):
        return self.solid_list
    def get_enterable(self):
        return self.entrance_list
    def hostile(self):
        return False
    def render(self): 
        self.game.screen.blit(self.land_map, self.rect)

class CaveMap(object):
    def __init__(self, parent):
        self.game = parent
        self.tile = Tile()
        self.all_sprites = pygame.sprite.Group()
        self.solid_list = pygame.sprite.Group()
        self.entrance_list = pygame.sprite.Group()

        self.cave_floor_map = pygame.Surface((640,320))
        self.rect = self.cave_floor_map.get_rect()

        self.tile_array = [
                "22221111111112222221",
                "22221111111112222221",
                "22221111111112222221",
                "22221111111111111111",
                "22221111111111111111",
                "22221111111112222222",
                "22221111111112222222",
                "22222221111112222222",
                "22222221111112222222",
                "11111111111111111111"]
        self.tile_array_1 = [
                "dddddddddddddddddddd",
                "00000000000000000000",
                "00000000000000000000",
                "00000000000000000000",
                "00000000000000000000",
                "00000000000000000000",
                "00000000000000000000",
                "00000000000000000000",
                "00000000000000000000",
                "bbbbbbbbbbbbbbbbbbbb"]
        self.tile_array_2 = [
                "c0000000000000c000aa",
                "c000000000000000000a",
                "c0000000000000c000aa",
                "c000000000000000000a",
                "c000000000000000000a",
                "c000000000000000000a",
                "c000000000000000000a",
                "c000000000000000000a",
                "c000000000000000000a",
                "c000000000000000000a"]
        self.load_tiles()

        self.render_tiles(self.cave_floor_map, self.tile_array)
        self.render_tiles(self.cave_floor_map, self.tile_array_1)
        self.render_tiles(self.cave_floor_map, self.tile_array_2)
        

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
                elif col == '2':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CaveWalls", x, y)
                elif col == 'a':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("RightBorder", x, y)
                elif col == 'b':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BottomBorder", x, y)
                elif col == 'c':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("LeftBorder", x, y)
                elif col == 'd':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("TopBorder", x, y)
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
            self.all_sprites.add(self.rock)
            self.solid_list.add(self.rock)
        elif solid == "CaveWalls":
            self.cave_walls = CaveWalls(x,y)
            self.all_sprites.add(self.cave_walls)
            self.solid_list.add(self.cave_walls)
        elif solid == "LeftBorder":
            self.left = Left(x,y)
            self.all_sprites.add(self.left)
            self.solid_list.add(self.left)
        elif solid == "RightBorder":
            self.right = Right(x,y)
            self.all_sprites.add(self.right)
            self.solid_list.add(self.right)
        elif solid == "BottomBorder":
            self.bottom = Bottom(x,y)
            self.all_sprites.add(self.bottom)
            self.solid_list.add(self.bottom)
        elif solid == "TopBorder":
            self.top = Top(x,y)
            self.all_sprites.add(self.top)
            self.solid_list.add(self.top)
        else:
            print "None" 
    def get_all_sprites(self):
        return self.all_sprites
    def get_solids(self):
        return self.solid_list
    def get_enterable(self):
        return self.entrance_list
    def hostile(self):
        return True
    def render(self):
        self.game.screen.blit(self.cave_floor_map, self.rect)
