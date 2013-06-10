# -*- coding: utf-8 -*-
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
        self.land_map = pygame.Surface((1600,640))
        self.rect = self.land_map.get_rect()

        #DEBUG TILE ARRAYS
        self.land_layer = []
        for w in range(32):
            self.land_layer.append("1"*32)

        self.tile_layer_1 = [
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",
                "11111111111111111111111111111111111111111111111111",]

        self.tile_layer_2 = [
                "23333333333333333333333333333333333333333333333334",
                "50000000000000000000000000000000000000000000000006",
                "!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#",
                "$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&",
                "*(((((((((((((((((((((((((((((((((((((((((((((((()",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",]

        self.tile_layer_3 = [
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "50000000000000000000000000000000000000000000000006",
                "accccccccccccccccccccccccccccccgcccccccccccccccccb",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",]
        self.tile_layer_4 = [
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "000000009hij00000000000000000000000000000000000000",
                "00000000klmn00000000000000000000000000000000000000",
                "00000000opqr00000000000000000000000000000000000000",
                "00000000stuv00000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",]
        self.tile_layer_5 = [
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "0000000000000000000000000000000000000000000+[]0000",
                "000000000000+]+[00000000\00{0000000_00000000000_00",
                "00000000000000+0]00000000wx}}000000000000000000000",
                "0000000000000000000000000yz{0\0000000000000-000000",
                "0009hij0000000000000000000000000000000000000000000",
                "000klmn0000780000000000000000000000|:;<00000000000",
                "000opqr000008080000000=000000000000////00000000000",
                "000stuv00070080000000000000,.>?000000000000`000000",
                "000000000008000000000000000////000000000000~000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",]
        self.map_border = [
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",
                "f000000000000000000000000000000000000000000000000d",]
        self.map_border_1 = [
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",]


        self.load_tiles()

        #TEMP LAYER RENDERING
        self.render_tiles(self.land_map, self.land_layer)
        self.render_tiles(self.land_map, self.tile_layer_1)
        self.render_tiles(self.land_map, self.tile_layer_2)
        self.render_tiles(self.land_map, self.tile_layer_3)
        self.render_tiles(self.land_map, self.tile_layer_4)
        self.render_tiles(self.land_map, self.map_border)
        self.render_tiles(self.land_map, self.map_border_1)

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
                elif col == '7':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BerryBush", x, y)
                elif col == '8':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("Bush", x, y)
                elif col == '9':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeOne", x, y)
                elif col == 'h':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeTwo", x, y)
                elif col == 'i':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeThree", x, y)
                elif col == 'j':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeFour", x, y)
                elif col == 'k':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeFive", x, y)
                elif col == 'l':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeSix", x, y)
                elif col == 'm':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeSeven", x, y)
                elif col == 'n':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeEight", x, y)
                elif col == 'o':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeNine", x, y)
                elif col == 'p':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeTen", x, y)
                elif col == 'q':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeEleven", x, y)
                elif col == 'r':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeTwelve", x, y)
                elif col == 's':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeThirteen", x, y)
                elif col == 't':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeFourteen", x, y)
                elif col == 'u':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeFifteen", x, y)
                elif col == 'v':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("BigTreeSixteen", x, y)
                elif col == 'w':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("LargeLogsOne", x, y)
                elif col == 'x':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("LargeLogsTwo", x, y)
                elif col == 'y':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("LargeLogsThree", x, y)
                elif col == 'z':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("LargeLogsFour", x, y)
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
                elif col == '!':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeLeftTop", x, y)
                elif col == '@':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeMiddleTop", x, y)
                elif col == '#':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeRightTop", x, y)
                elif col == '$':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeLeftCenter", x, y)
                elif col == '%':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeMiddleCenter", x, y)
                elif col == '&':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeRightCenter", x, y)
                elif col == '*':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeLeftBottom", x, y)
                elif col == '(':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeMiddleBottom", x, y)
                elif col == ')':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("CliffSideLargeRightBottom", x, y)
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
                elif col == '-':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsOne", x, y)
                elif col == '_':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsTwo", x, y)
                elif col == '=':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsThree", x, y)
                elif col == '+':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsFour", x, y)
                elif col == '[':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsFive", x, y)
                elif col == ']':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsSix", x, y)
                elif col == '{':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsSeven", x, y)
                elif col == '}':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsEight", x, y)
                elif col == '\\':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("ObjectsNine", x, y)
                elif col == '|':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandOne", x, y)
                elif col == ':':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandTwo", x, y)
                elif col == ';':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandThree", x, y)
                elif col == '<':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandFour", x, y)
                elif col == ',':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandFive", x, y)
                elif col == '.':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandSix", x, y)
                elif col == '>':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandSeven", x, y)
                elif col == '?':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandEight", x, y)
                elif col == '/':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("FoodStandBottomOne", x, y)
                elif col == '`':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("SmallTableOne", x, y)
                elif col == '~':
                    x = 32*(tile_column - 1)
                    y = 32*(tile_row - 1)
                    self.render_solids("SmallTableTwo", x, y)
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
        elif solid == "BerryBush":
            self.berrybush = BerryBush(x,y)
            self.all_sprites.add(self.berrybush)
            self.solid_list.add(self.berrybush)
        elif solid == "Bush":
            self.bush = Bush(x,y)
            self.all_sprites.add(self.bush)
            self.solid_list.add(self.bush)
        elif solid == "BigTreeOne":
            self.big_tree_one = BigTreeOne(x,y)
            self.all_sprites.add(self.big_tree_one)
            self.solid_list.add(self.big_tree_one)
        elif solid == "BigTreeTwo":
            self.big_tree_two = BigTreeTwo(x,y)
            self.all_sprites.add(self.big_tree_two)
            self.solid_list.add(self.big_tree_two)
        elif solid == "BigTreeThree":
            self.big_tree_three = BigTreeThree(x,y)
            self.all_sprites.add(self.big_tree_three)
            self.solid_list.add(self.big_tree_three)
        elif solid == "BigTreeFour":
            self.big_tree_four = BigTreeFour(x,y)
            self.all_sprites.add(self.big_tree_four)
            self.solid_list.add(self.big_tree_four)
        elif solid == "BigTreeFive":
            self.big_tree_five = BigTreeFive(x,y)
            self.all_sprites.add(self.big_tree_five)
            self.solid_list.add(self.big_tree_five)
        elif solid == "BigTreeSix":
            self.big_tree_six = BigTreeSix(x,y)
            self.all_sprites.add(self.big_tree_six)
            self.solid_list.add(self.big_tree_six)
        elif solid == "BigTreeSeven":
            self.big_tree_seven = BigTreeSeven(x,y)
            self.all_sprites.add(self.big_tree_seven)
            self.solid_list.add(self.big_tree_seven)
        elif solid == "BigTreeEight":
            self.big_tree_eight = BigTreeEight(x,y)
            self.all_sprites.add(self.big_tree_eight)
            self.solid_list.add(self.big_tree_eight)
        elif solid == "BigTreeNine":
            self.big_tree_nine = BigTreeNine(x,y)
            self.all_sprites.add(self.big_tree_nine)
            self.solid_list.add(self.big_tree_nine)
        elif solid == "BigTreeTen":
            self.big_tree_ten = BigTreeTen(x,y)
            self.all_sprites.add(self.big_tree_ten)
            self.solid_list.add(self.big_tree_ten)
        elif solid == "BigTreeEleven":
            self.big_tree_eleven = BigTreeEleven(x,y)
            self.all_sprites.add(self.big_tree_eleven)
            self.solid_list.add(self.big_tree_eleven)
        elif solid == "BigTreeTwelve":
            self.big_tree_twelve = BigTreeTwelve(x,y)
            self.all_sprites.add(self.big_tree_twelve)
            self.solid_list.add(self.big_tree_twelve)
        elif solid == "BigTreeThirteen":
            self.big_tree_thirteen = BigTreeThirteen(x,y)
            self.all_sprites.add(self.big_tree_thirteen)
            self.solid_list.add(self.big_tree_thirteen)
        elif solid == "BigTreeFourteen":
            self.big_tree_fourteen = BigTreeFourteen(x,y)
            self.all_sprites.add(self.big_tree_fourteen)
            self.solid_list.add(self.big_tree_fourteen)
        elif solid == "BigTreeFifteen":
            self.big_tree_fifteen = BigTreeFifteen(x,y)
            self.all_sprites.add(self.big_tree_fifteen)
            self.solid_list.add(self.big_tree_fifteen)
        elif solid == "BigTreeSixten":
            self.big_tree_sixteen = BigTreeSixteen(x,y)
            self.all_sprites.add(self.big_tree_sixteen)
            self.solid_list.add(self.big_tree_sixteen)
        elif solid == "LargeLogsOne":
            self.large_logs_one = LargeLogsOne(x,y)
            self.all_sprites.add(self.large_logs_one)
            self.solid_list.add(self.large_logs_one)
        elif solid == "LargeLogsTwo":
            self.large_logs_two = LargeLogsTwo(x,y)
            self.all_sprites.add(self.large_logs_two)
            self.solid_list.add(self.large_logs_two)
        elif solid == "LargeLogsThree":
            self.large_logs_three = LargeLogsThree(x,y)
            self.all_sprites.add(self.large_logs_three)
            self.solid_list.add(self.large_logs_three)
        elif solid == "LargeLogsFour":
            self.large_logs_four = LargeLogsFour(x,y)
            self.all_sprites.add(self.large_logs_four)
            self.solid_list.add(self.large_logs_four)
        elif solid == "ObjectsOne":
            self.objects_one = ObjectsOne(x,y)
            self.all_sprites.add(self.objects_one)
            self.solid_list.add(self.objects_one)
        elif solid == "ObjectsTwo":
            self.objects_two = ObjectsTwo(x,y)
            self.all_sprites.add(self.objects_two)
            self.solid_list.add(self.objects_two)
        elif solid == "ObjectsThree":
            self.objects_three = ObjectsThree(x,y)
            self.all_sprites.add(self.objects_three)
            self.solid_list.add(self.objects_three)
        elif solid == "ObjectsFour":
            self.objects_four = ObjectsFour(x,y)
            self.all_sprites.add(self.objects_four)
            self.solid_list.add(self.objects_four)
        elif solid == "ObjectsFive":
            self.objects_five = ObjectsFive(x,y)
            self.all_sprites.add(self.objects_five)
            self.solid_list.add(self.objects_five)
        elif solid == "ObjectsSix":
            self.objects_six = ObjectsSix(x,y)
            self.all_sprites.add(self.objects_six)
            self.solid_list.add(self.objects_six)
        elif solid == "ObjectsSeven":
            self.objects_seven = ObjectsSeven(x,y)
            self.all_sprites.add(self.objects_seven)
            self.solid_list.add(self.objects_seven)
        elif solid == "ObjectsEight":
            self.objects_eight = ObjectsEight(x,y)
            self.all_sprites.add(self.objects_eight)
            self.solid_list.add(self.objects_eight)
        elif solid == "ObjectsNine":
            self.objects_nine = ObjectsNine(x,y)
            self.all_sprites.add(self.objects_nine)
            self.solid_list.add(self.objects_nine)
        elif solid == "FoodStandOne":
            self.food_stand_one = FoodStandOne(x,y)
            self.all_sprites.add(self.food_stand_one)
            self.solid_list.add(self.food_stand_one)
        elif solid == "FoodStandTwo":
            self.food_stand_two = FoodStandTwo(x,y)
            self.all_sprites.add(self.food_stand_two)
            self.solid_list.add(self.food_stand_two)
        elif solid == "FoodStandThree":
            self.food_stand_three = FoodStandOne(x,y)
            self.all_sprites.add(self.food_stand_three)
            self.solid_list.add(self.food_stand_three)
        elif solid == "FoodStandFour":
            self.food_stand_four = FoodStandFour(x,y)
            self.all_sprites.add(self.food_stand_four)
            self.solid_list.add(self.food_stand_four)
        elif solid == "FoodStandFive":
            self.food_stand_five = FoodStandFive(x,y)
            self.all_sprites.add(self.food_stand_five)
            self.solid_list.add(self.food_stand_five)
        elif solid == "FoodStandSix":
            self.food_stand_six = FoodStandSix(x,y)
            self.all_sprites.add(self.food_stand_six)
            self.solid_list.add(self.food_stand_six)
        elif solid == "FoodStandSeven":
            self.food_stand_seven = FoodStandSeven(x,y)
            self.all_sprites.add(self.food_stand_seven)
            self.solid_list.add(self.food_stand_seven)
        elif solid == "FoodStandEight":
            self.food_stand_eight = FoodStandEight(x,y)
            self.all_sprites.add(self.food_stand_eight)
            self.solid_list.add(self.food_stand_eight)
        elif solid == "FoodStandBottomOne":
            self.food_stand_bottom_one = FoodStandBottomOne(x,y)
            self.all_sprites.add(self.food_stand_bottom_one)
            self.solid_list.add(self.food_stand_bottom_one)
        elif solid == "SmallTableOne":
            self.small_table_one = SmallTableOne(x,y)
            self.all_sprites.add(self.small_table_one)
            self.solid_list.add(self.small_table_one)
        elif solid == "SmallTableTwo":
            self.small_table_two = SmallTableTwo(x,y)
            self.all_sprites.add(self.small_table_two)
            self.solid_list.add(self.small_table_two)
        elif solid == "CliffSideLargeLeftTop":
            self.cliff_side_large_left_top = CliffSideLargeLeftTop(x,y)
            self.all_sprites.add(self.cliff_side_large_left_top)
            self.solid_list.add(self.cliff_side_large_left_top)
        elif solid == "CliffSideLargeMiddleTop":
            self.cliff_side_large_middle_top = CliffSideLargeMiddleTop(x,y)
            self.all_sprites.add(self.cliff_side_large_middle_top)
            self.solid_list.add(self.cliff_side_large_middle_top)
        elif solid == "CliffSideLargeRightTop":
            self.cliff_side_large_right_top = CliffSideLargeRightTop(x,y)
            self.all_sprites.add(self.cliff_side_large_right_top)
            self.solid_list.add(self.cliff_side_large_right_top)
        elif solid == "CliffSideLargeLeftCenter":
            self.cliff_side_large_left_center = CliffSideLargeLeftCenter(x,y)
            self.all_sprites.add(self.cliff_side_large_left_center)
            self.solid_list.add(self.cliff_side_large_left_center)
        elif solid == "CliffSideLargeMiddleCenter":
            self.cliff_side_large_middle_center = CliffSideLargeMiddleCenter(x,y)
            self.all_sprites.add(self.cliff_side_large_middle_center)
            self.solid_list.add(self.cliff_side_large_middle_center)
        elif solid == "CliffSideLargeRightCenter":
            self.cliff_side_large_right_center = CliffSideLargeRightCenter(x,y)
            self.all_sprites.add(self.cliff_side_large_right_center)
            self.solid_list.add(self.cliff_side_large_right_center)
        elif solid == "CliffSideLargeLeftBottom":
            self.cliff_side_large_left_bottom = CliffSideLargeLeftBottom(x,y)
            self.all_sprites.add(self.cliff_side_large_left_bottom)
            self.solid_list.add(self.cliff_side_large_left_bottom)
        elif solid == "CliffSideLargeMiddleBottom":
            self.cliff_side_large_middle_bottom = CliffSideLargeMiddleBottom(x,y)
            self.all_sprites.add(self.cliff_side_large_middle_bottom)
            self.solid_list.add(self.cliff_side_large_middle_bottom)
        elif solid == "CliffSideLargeRightBottom":
            self.cliff_side_large_right_bottom = CliffSideLargeRightBottom(x,y)
            self.all_sprites.add(self.cliff_side_large_right_bottom)
            self.solid_list.add(self.cliff_side_large_right_bottom)
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

        self.cave_floor_map = pygame.Surface((1600,640))
        self.rect = self.cave_floor_map.get_rect()

        self.tile_array = [
                "22211111111222222222222222222222222111111122222222",
                "22211111111222222222222222222222222111111122222222",
                "22211111111111111111122222222222222111111122222222",
                "22211111111111111111122222222222222111111122222222",
                "22211111111111111111122222222222222111111122222222",
                "22222222222222222111111111111111111111111111111111",
                "22222222222222222111111111111111111111111111111111",
                "22222221111111111111112222222222222222222222211111",
                "22222221111111111111112222222222222222222222211111",
                "22111111111222222111112222222222222222222222211111",
                "22111111111222222111112222222222222222222222211111",
                "22111111111222222111112222222222222222222222211111",
                "11111111111222222111112222222222222222222222211111",
                "11111111111222222111112222222222222222222222211111",
                "11111222222222211111111111111111111111111111111111",
                "11111222222222211111111111111111111111111111111111",
                "11111222222222211111111111111111111111111111111111",
                "11111222222222211111111122222222222222222222222222",
                "11111111111111111111222222222222222222222222222222",
                "11111111111111111111222222222222222222222222222222",]
        self.tile_array_1 = [
                "dddddddddddddddddddddddddddddddddddddddddddddddddd",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "00000000000000000000000000000000000000000000000000",
                "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",]
        self.tile_array_2 = [
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",
                "c000000000000000000000000000000000000000000000000a",]
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
