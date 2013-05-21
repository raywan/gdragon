import sys
import pygame
from sprites import *
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
        self.player = Player(self.game, (250,250))
        self.map_1 = Map(self.game)
        self.map_1.render_tiles((0,0))

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
        self.player.update()
        
        #SIMULATES A CAMERA
        # if self.player.rect.x > 500:
        #     self.map_1.rect.x -= 2
        #     self.player.rect.x = 500
        # elif self.player.rect.x < 140:
        #     self.map_1.rect.x += 2
        #     self.player.rect.x = 140

        # elif self.player.rect.y < 140:
        #     self.map_1.rect.y += 2
        #     self.player.rect.y = 140
        # elif self.player.rect.y > 340:
        #     self.map_1.rect.y -= 2
        #     self.player.rect.y = 340

        pygame.display.flip()

    def render(self):
        self.game.screen.blit(self.play_surf, (0,0))
        self.map_1.render_map()
        self.player.render()
    def on_enter(self, args):
        pass
    def on_exit(self):
        pass

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
