from typing import List

class WallEnum:
    EMPTY = 0
    WALL = 1
    
class Map:
    @classmethod
    def set_map(cls, map: List[List[WallEnum]]) -> None:
        cls.map = map
        
    @classmethod
    def get(cls, x,y):
        return cls.map[x][y]
    
    @classmethod
    def is_wall(cls, x,y):
        x ,y = int(x), int(y)
        return cls.map[x][y] == WallEnum.WALL 
    
