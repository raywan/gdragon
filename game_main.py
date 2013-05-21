import sys
import pygame
from pygame.locals import *
from game_states import *
from sprites import *

class StateManager(object):
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

#Might use later
class Screen(object):
    def __init__(self, w, h):
        pass

class Game(object):
    def __init__(self):
        self.running = True
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.SCALE = 3
    def on_init(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        self.ss = SpriteSheet("test.png")
        self.game_state = StateManager()
        self.game_state.add("main", MainMenu(self))
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

def main():
    game = Game()
    game.on_exec()

if __name__ == "__main__":
    main()
