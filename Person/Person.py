from typing import Tuple, List
import numpy as np

class Person:
    """ Class of each person of we will be detected  """
    
    color_id_and_cout_of_person = 0 # id box tracker color of person and also it is count of all people on video
    
    def __init__(self, ids: int, x: int, y: int, w: int, h: int) -> None:
        """ Contructor """
        Person.color_id_and_cout_of_person += 1
        np.random.seed(Person.color_id_and_cout_of_person)
        self.ids: int = ids
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.R = np.random.randint(255)
        self.G = np.random.randint(255)
        self.B = np.random.randint(255)
        self.cx = int(x + w / 2) # Cast to int because pixel can't be a fractional
        self.cy = int(y + h / 2) # Cast to int because pixel can't be a fractional
        self.trace = [(self.cx, self.cy)]
        
    def get_id(self) -> int:
        """ Getter of id person """       
        return self.ids
    
    def get_box_coordinates(self) -> Tuple[int, int, int, int]:
        """ Get coordinates of person """
        return self.x, self.y, self.w, self.h
    
    def get_centre_box(self) -> Tuple[int, int]:
        """ Get centre of person box """
        return self.cx, self.cy
    
    def get_trace(self) -> List[Tuple[int, int]]:
        """ Get trace of person """
        return self.trace
    
    def get_x(self) -> int:
        """ Get x coordinate """
        return self.x
    
    def get_y(self) -> int:
        """ Get y coordinate """
        return self.y
    
    def update_coordinates(self, nx: int, ny: int, nw: int, nh: int) -> None:
        """ Update coordinates of person """
        self.x = nx
        self.y = ny
        self.w = nw
        self.h = nh
        self.cx = int(nx + nw / 2) # Cast to int because pixel can't be a fractional
        self.cy = int(ny + nh / 2) # Cast to int because pixel can't be a fractional
        self.trace.append((self.cx, self.cy))
