from aifc import Aifc_read
from random import randint, choice
import texture
from tkinter import NW

AIR = 'a'
BLOCK_SIZE = 64
AIR = 'a'
GROUND = 'g'
WATER = 'w'
CONCRETE = 'c'
BRICK = 'b'
_camera_x = 0
_camera_y = 0
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WIDTH = SCREEN_WIDTH * 6
HEIGHT = SCREEN_HEIGHT * 4
_canvas = None
_map = []

def get_block(row, col):
    if row < 0 or col < 0 or row >= get_rows() \
            or col >= get_cols():
        return AIR
    else:
        return _map[row][col].get_block()

def update_cell(row, col):
    if row < 0 or col < 0 or row >= get_rows() or col >= get_cols():
        return
    _map[row][col].update()

def update_map(all=False):
    first_row = get_row(_camera_y)
    last_row = get_row(_camera_y + SCREEN_HEIGHT - 1)
    first_col = get_col(_camera_x)
    last_col = get_col(_camera_x + SCREEN_WIDTH - 1)
    if all:
        first_row = 0
        first_col = 0
        last_row = get_rows()-1
        last_col = get_cols()-1
    for i in range(first_row, last_row + 1):
        for j in range(first_col, last_col + 1):
            update_cell(i, j)



def get_row(y):
    return int(y)//BLOCK_SIZE

def get_col(x):
    return int(x)//BLOCK_SIZE



def get_rows():
    return len(_map)

def get_cols():
    return len(_map[0])

def get_width():
    return get_cols() * BLOCK_SIZE

def get_height():
    return get_rows() * BLOCK_SIZE

def create_map(rows = 20, cols = 20):
    global _map
    _map = []
    for i in range(rows):
        row = []
        for j in range(cols):
            block = GROUND
            if i == 0 or j == 0 or i == rows - 1 or j == cols - 1:
                block = CONCRETE
            elif randint(1, 100) <= 15:
                block = choice([BRICK, WATER, CONCRETE])
            cell = _Cell(BLOCK_SIZE * j, BLOCK_SIZE * i,block, _canvas)
            row.append(cell)
        _map.append(row)

def initialize(canv):
    global _canvas
    _canvas = canv
    create_map(20, 20)



def set_camera_xy(x, y):
    global _camera_x, _camera_y
    if x < 0:
        x = 0

    if y < 0:
        y = 0

    if x > get_width() - SCREEN_WIDTH:
        x = get_width() - SCREEN_WIDTH

    if y > get_height() - SCREEN_HEIGHT:
        y = get_height() - SCREEN_HEIGHT

    _camera_x = x
    _camera_y = y

    update_all = False
    if abs(_camera_x - x) >= BLOCK_SIZE or  abs (_camera_y - y) >= BLOCK_SIZE:
        update_all = True
    _camera_x = x
    _camera_y = y

    if update_all:
        update_map(all=True)



def move_camera(delta_x, delta_y):
    set_camera_xy(_camera_x + delta_x, _camera_y + delta_y)

def get_screen_x(world_x):
        return world_x - _camera_x

def get_screen_y(world_y):
    return world_y - _camera_y

def get_block(row, col):
    if row < 0 or col < 0 or row >= get_rows() \
        or col >= get_cols():
        return AIR
    else:
        return _map[row][col].get_block()

class _Cell:
   def __init__(self, x, y, block, canvas):
          self.__x = x
          self.__y = y
          self.__screen_x = get_screen_x(x)
          self.__screen_y = get_screen_y(y)
          self.__canvas = canvas
          self.__block = block
          self.__create_element(block)

   def update(self):
       if self.__block == GROUND:
           return
       screen_x = get_screen_x(self.__x)
       screen_y = get_screen_y(self.__y)
       if self.__screen_x == screen_x and self.__screen_y == screen_y:
           return
       self.__canvas.moveto(self.__id, x=screen_x, y=screen_y)
       self.__screen_x = screen_x
       self.__screen_y = screen_y


   def __create_element(self, block):
       if block != GROUND:
           self.__id = self.__canvas.create_image(self.__screen_x, self.__screen_y,
                                                  image = texture.get(block), anchor = NW)

   def __del__(self):
       try:
           self.__canvas.delete(self.__id)
       except:
           pass

   def get_block(self):
       return self.__block



