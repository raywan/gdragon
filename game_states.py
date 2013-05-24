import sys
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
        self.player = Player(self.game, (250,250))

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
        self.player.update(self.current_map.get_solids())

        #SIMULATES A CAMERA
        if self.player.rect.x > 500:
            diff = self.player.rect.x - 500
            self.current_map.rect.x -= diff
            self.player.rect.x = 500
            for solids in self.current_map.get_solids():
                solids.rect.x -= diff

        elif self.player.rect.x < 140:
            diff = 140 - self.player.rect.x
            self.current_map.rect.x += diff
            self.player.rect.x = 140
            for solids in self.current_map.get_solids():
                solids.rect.x += diff

        if self.player.rect.y < 140:
            diff = 140 - self.player.rect.y
            self.current_map.rect.y += 2
            self.player.rect.y = 140
            for solids in self.current_map.get_solids():
                solids.rect.y += diff
        elif self.player.rect.y > 340:
            diff = self.player.rect.y - 340
            self.current_map.rect.y -= diff
            self.player.rect.y = 340
            for solids in self.current_map.get_solids():
                solids.rect.y -= diff

        pygame.display.flip()

    def render(self):
        self.game.screen.blit(self.play_surf, (0,0))
        self.current_map.render()
        self.current_map.get_solids().draw(self.game.screen)
        self.player.render()
    def on_enter(self, args):
        pass
    def on_exit(self):
        pass
    def change_map(self, m):
        if m == "main":
            self.main_map = MainMap(self.game, 0,0)
            return self.main_map

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
