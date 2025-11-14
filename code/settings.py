import pygame 
from os.path import join 
from os import walk
import os

GAME_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 
TILE_SIZE = 64