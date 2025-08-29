import pygame
from os.path import join
from random import randint, uniform
from os import walk
from support import *
from dataclasses import dataclass, field
from groups import *


WINDOW_WIDTH: int
WINDOW_HEIGHT: int = 1280, 720
FPS: int = 60
