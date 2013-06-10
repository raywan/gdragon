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
        """
        FCN NAME: event
        DESCRIPTION: Runs the event method for the current state
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.current_state.event()
    def update(self):
        """
        FCN NAME: update
        DESCRIPTION: Runs the update method for the current state
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.current_state.update()
    def render(self):
        """
        FCN NAME: render
        DESCRIPTION: Runs the render method for the current state
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.current_state.render()
    def change(self, state_name, other_args):
        """
        FCN NAME: change
        DESCRIPTION: Changes the current state to the state specified
        INPUTS: State Name - state_name
                Other Arguments - other_args
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.current_state.on_exit()
        self.current_state = self.states[state_name]
        self.current_state.on_enter(other_args)
    def add(self, state_name, state_class):
        """
        FCN NAME: add
        DESCRIPTION: Adds a state to the state stack using key-pair values
        INPUTS: State Name - state_name
                State Class - state_class
        OUTPUTS: None
        ALGORITHMS: None
        """
        #list_of_states[state_name] = state_class
        self.states[state_name] = state_class
    def pop(self, state_name):
        """
        FCN NAME: pop 
        DESCRIPTION: Pops the specified state out of the stack
        INPUTS: State Name - state_name
        OUTPUTS: None
        ALGORITHMS: None
        """
        #pop a state off the stack
        self.states.pop(state_name)

class Game(object):
    def __init__(self):
        """
        FCN NAME: __init__
        DESCRIPTION: Sets constants
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.running = True
        self.FPS = 60
        self.FRAMES = self.FPS/12
        self.SCREEN_WIDTH = 640
        self.SCREEN_HEIGHT = 480
        self.SCALE = 3
    def on_init(self):
        """
        FCN NAME: on_init
        DESCRIPTION: A method that initializes various aspects of the game
                For example, the screen size, and adding states into the stack.
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        pygame.init()
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)
        self.clock = pygame.time.Clock()

        self.game_state = StateManager()
        self.game_state.add("main", MainMenu(self))
        self.game_state.change("main", None)
        
    def on_event(self):
        """
        FCN NAME: on_event
        DESCRIPTION: Runs the events in the current state
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.game_state.event()
    def on_update(self):
        """
        FCN NAME: on_update
        DESCRIPTION: Runs the updates in the current state
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.game_state.update()
    def on_render(self):
        """
        FCN NAME: on_render
        DESCRIPTION: Renders all renderable objects in the current state
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.game_state.render()
    def on_exec(self):
        """
        FCN NAME: on_exec
        DESCRIPTION: The main loop of the game, loops through the event, update and render methods
        INPUTS: None
        OUTPUTS: None
        ALGORITHMS: None
        """
        self.on_init()

        while self.running:
            self.clock.tick(self.FPS)
            self.on_event()
            self.on_update()
            self.on_render()
