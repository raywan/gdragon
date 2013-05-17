import sys
import pygame
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
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    self.game.game_state.change("play", None)
    def update(self):
        pygame.display.flip()
    def render(self):
        self.game.screen.blit(self.main_surf, (0,0))
    def on_enter(self, args):
        self.main_surf = pygame.Surface((300,200), 0, 32)
    def on_exit(self):
        pass

class Play(object):
    def __init__(self, parent):
        self.game = parent
    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_m:
                    self.game.game_state.change("main", None)
    def update(self):
        pygame.display.flip()
    def render(self):
        self.game.screen.blit(self.play_surf, (0,0))
    def on_enter(self, args):
        self.play_surf = pygame.Surface((300,200), 0, 32)
        self.play_surf.fill((250,250,250))
    def on_exit(self):
        pass

class StateMachine(object):
    #list of states
    empty_state = EmptyState(None)
    current_state = empty_state
    states = {}
    def event(self):
        self.current_state.event()
    def update(self):
        self.current_state.update()
    def render(self):
        self.current_state.render()
    def change(self, state_name, other_args):
        self.current_state.on_exit()
        self.current_state = self.states[state_name]
        self.current_state.on_enter(other_args)
    def add(self, state_name, state_class):
        #list_of_states[state_name] = state_class
        self.states[state_name] = state_class
    def pop(self, state_name):
        #pop a state off the stack
        self.states.pop(state_name)

class StateStack(object):
    #list of states
    states = {}
    def event(self):
        # self.current_state.event()
        pass
    def update(self):
        #update top stack
        # self.top_state.update()
        pass
    def render(self):
        #like update, render top stack
        # self.top_state.render()
        pass
    def change(self, state_name, other_args):
        pass
    def push(self, state_name, state_class):
        #pushes a state into the state stack
        #list_of_states.Push(state)
        pass
    def pop(self):
        #pop a state off the stack
        #state.Pop()
        pass

class Game(object):
    def __init__(self):
        self.running = True
        self.SCREEN_WIDTH = 300
        self.SCREEN_HEIGHT = 200
    def on_init(self):
        #set screen and load stuff
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        self.game_state = StateMachine()
        self.game_state.add("main", MainMenu(self))
        self.game_state.add("play", Play(self))
        self.game_state.change("main", None)
        
    def on_event(self):
        self.game_state.event()
    def on_update(self):
        self.game_state.update()
    def on_render(self):
        self.game_state.render()

    def on_exec(self):
        self.on_init()

        while self.running:
            self.clock.tick(60)
            self.on_event()
            self.on_update()
            self.on_render()
        #self.on_cleanup()

def main():
    game = Game()
    game.on_exec()

if __name__ == "__main__":
    main()
