import sys
import random
import pygame
from sprites import *
from level import *
from pygame.locals import *

#To be interfaced from
class EmptyState(object):
    def __init__(self, parent):
        pass
    def update(self):
        pass
    def render(self, screen):
        pass
    def on_enter(self, args):
        pass
    def on_exit(self):
        pass

class MainMenu(object):
    def __init__(self, parent):
        self.game = parent

        self.main_surf = pygame.Surface((800,600), 0, 32)
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    try:
                        self.game.game_state.change("play", None)
                    except KeyError:
                        self.game.game_state.add("play", Play(self.game))
                        self.game.game_state.change("play", None)

                #DEBUG########
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()
                ##############
    def update(self):
        pygame.display.flip()
    def render(self):
        self.game.screen.blit(self.main_surf, (0,0))
    def on_enter(self, args):
        pass
    def on_exit(self):
        pass

class Play(object):
    def __init__(self, parent):
        self.game = parent

        self.play_surf = pygame.Surface((800,600), 0, 32)
        self.play_surf.fill((250,250,250))
        self.current_map = self.change_map("main")
        self.player = Player(self, (250,250))

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                #DEBUG########
                if event.key == K_m:
                    self.game.game_state.change("main", None)
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_c:
                    self.current_map = self.change_map("cave")
                elif event.key == K_v:
                    self.current_map = self.change_map("main")
                ##############
                elif event.key == K_DOWN:
                    self.player.move(0,2)
                elif event.key == K_UP:
                    self.player.move(0,-2)
                elif event.key == K_RIGHT:
                    self.player.move(2,0)
                elif event.key == K_LEFT:
                    self.player.move(-2,0)
            elif event.type == KEYUP:
                if event.key == K_DOWN:
                    self.player.move(0,-2)
                elif event.key == K_UP:
                    self.player.move(0,2)
                elif event.key == K_RIGHT:
                    self.player.move(-2,0)
                elif event.key == K_LEFT:
                    self.player.move(2,0)

    def update(self):
        self.player.update(self.current_map.get_solids(), self.current_map.get_enterable())

        #SIMULATES A CAMERA
        #checks for x-pos
        if self.player.rect.x > 500:
            diff = self.player.rect.x - 500
            self.current_map.rect.x -= diff
            if self.current_map == self.main_map:
                # self.current_map.outer_water_map_rect.x -= diff
                pass
            self.player.rect.x = 500
            for solids in self.current_map.get_all_sprites():
                solids.rect.x -= diff
        elif self.player.rect.x < 140:
            diff = 140 - self.player.rect.x
            self.current_map.rect.x += diff
            if self.current_map == self.main_map:
                # self.current_map.outer_water_map_rect.x += diff
                pass
            self.player.rect.x = 140
            for solids in self.current_map.get_all_sprites():
                solids.rect.x += diff
        #checks for y-pos
        if self.player.rect.y < 140:
            diff = 140 - self.player.rect.y
            self.current_map.rect.y += 2
            if self.current_map == self.main_map:
                # self.current_map.outer_water_map_rect.y += diff
                pass
            self.player.rect.y = 140
            for solids in self.current_map.get_all_sprites():
                solids.rect.y += diff
        elif self.player.rect.y > 340:
            diff = self.player.rect.y - 340
            self.current_map.rect.y -= diff
            if self.current_map == self.main_map:
                # self.current_map.outer_water_map_rect.y -= diff
                pass
            self.player.rect.y = 340
            for solids in self.current_map.get_all_sprites():
                solids.rect.y -= diff

        #Checks if the map is hotile and does RNG if the player is moving
        if self.current_map.hostile():
            if self.player.is_moving():
                if self.generate_enemies() == 666:
                    try:
                        self.game.game_state.change("battle", None)
                    except KeyError:
                        self.game.game_state.add("battle", Battle(self))
                        self.game.game_state.change("battle", None)
                    self.player.d_x = 0
                    self.player.d_y = 0
            

        pygame.display.flip()

    def render(self):
        self.game.screen.blit(self.play_surf, (0,0))
        self.current_map.render()
        self.current_map.get_all_sprites().draw(self.game.screen)
        self.player.render()
    def on_enter(self, args):
        pass
    def on_exit(self):
        pass
    def change_map(self, m):
        if m == "main":
            self.main_map = MainMap(self.game)
            return self.main_map
        if m == "cave":
            self.cave_map = CaveMap(self.game)
            return self.cave_map
    def generate_enemies(self):
        return random.randint(1, 1000)

class Battle(object):
    def __init__(self, parent):
        self.parent = parent
        self.surface = pygame.Surface((640,480))
        self.surface.fill((0,0,250))
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_e:
                    self.parent.game.game_state.change("play", None)
                #DEBUG########
                elif event.key == K_q:
                    pygame.quit()
                    sys.exit()
                ##############

    def update(self):
        pygame.display.flip()
    def render(self):
        self.parent.game.screen.blit(self.surface, (0,0))
    def on_enter(self, args):
        pass
    def on_exit(self):
        self.parent.game.game_state.pop("battle")

class Pause(object):
    def __init__(self, parent):
        self.game = parent
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def update(self):
        pass
        # pygame.display.flip()
    def render(self):
        pass
    def on_enter(self, args):
        pass
    def on_exit(self):
        pass
