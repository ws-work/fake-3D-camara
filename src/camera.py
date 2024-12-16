import math

from typing import Tuple

import util 
from pprint import pprint
from map import Map
from context import WIDTH, HEIGHT

class ScreenEnum:
    SKY = 0
    WALL_y = 1
    WALL_x = 2
    GROUND = 3
    
class Camera:
    SIGHT_SIZE = 60 # 视野宽带，设置为左右各60°
    screen = [[ScreenEnum.SKY]*WIDTH for _ in range(HEIGHT)]
    
    def __init__(self):
        self.position = (1,1)
        self.forward = 0  # 方向采用角度制，逆时针方向为增加
        
    def build_map(self):
        
        position = self.position
        forward = self.forward
        
        each_inver_degree = 2*self.SIGHT_SIZE / (WIDTH - 1) 
        lefest_degree = forward + self.SIGHT_SIZE
        for x in range(WIDTH):
            cur_degree = lefest_degree - x * each_inver_degree
            cur_pos = list(position)
            # 每次位移1，那么x方向和y方向的位移分别是dx，dy
            dx, dy = util.sin(cur_degree), util.cos(cur_degree)
            x_side = abs(dx) > abs(dy)
            dis = 0
            while not Map.is_wall(*cur_pos):
                cur_pos[0] += dx
                cur_pos[1] += dy
                dis += 1
            wall_height = HEIGHT // dis
            for y in range(int(HEIGHT//2 - wall_height // 2),HEIGHT):
                if y <= HEIGHT //2 + wall_height // 2:
                    self.screen[y][x] = ScreenEnum.WALL_x if x_side else ScreenEnum.WALL_y
                else:
                    self.screen[x][y] = ScreenEnum.GROUND
        for i in self.screen:
            for j in i:
                print(j,end='')
            print()
        return self.screen
    