import pygame 
from os.path import join, dirname, abspath
from os import walk

GAME_ROOT = abspath(join(dirname(abspath(__file__)), ".."))
WINDOW_WIDTH, WINDOW_HEIGHT = 1280,720 
TILE_SIZE = 64