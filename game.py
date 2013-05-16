import sys
import pygame
from pygame.locals import *

class EmptyState(object):
    def update(self):
        pass
    def render(self):
        pass
    def on_enter(self):
        pass
    def on_exit(self):
        pass

class StateMachine(object):
    #list of states
    #current_state = empty_state
    def update(self):
        #current_state.update()
        pass
    def render(self):
        #current_state.render()
        pass
    def change(self, state_name, other_args):
        #current_state.on_exit()
        #current_state = list_of_states[state_name]
        #current_state.on_enter(other_args)
        pass
    def add(self, state_name, state_class):
        #list_of_states[state_name] = state_class
        pass

class StateStack(object):
    #list of states
    def update(self):
        #update top stack
        #top.Update()
        #top being a State object
        pass
    def render(self):
        #like update, render top stack
        #top.Render()
        pass
    def push(self, state_name):
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
    def on_init(self):
        pygame.init()
        #set screen and load stuff
    def on_event(self):
        pass
    def on_update(self):
        #game_state.update()
        #game_state.render()
        pass
    def on_render(self):
        pass
    def on_exec(self):
        self.on_init()

        while self.running:
            clock.tick(60)
            # self.on_event()
            # self.on_loop()
            # self.on_render()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        # self.on_cleanup()


def main():
    game = Game()
    game.on_exec()
