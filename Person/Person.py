from typing import Tuple, List
import numpy as np

class Person:
    """ Class of each person of we will be detected  """
    
    color_id_and_cout_of_person = 0 # id box tracker color of person and also it is count of all people on video
    
    def __init__(self, ids: int, box: List[float]) -> None:
        """ Contructor """
        Person.color_id_and_cout_of_person += 1
        np.random.seed(Person.color_id_and_cout_of_person)
        self.ids = ids
        self.x = int(box[0])
        self.y = int(box[1])
        self.w = int(abs(box[0] - box[2]))
        self.h = int(abs(box[1] - box[3]))
        self.R = np.random.randint(255)
        self.G = np.random.randint(255)
        self.B = np.random.randint(255)
        self.cx = int(self.x + self.w / 2) # Cast to int because pixel can't be a fractional
        self.cy = int(self.y + self.h / 2) # Cast to int because pixel can't be a fractional
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
    
    def get_box(self) -> Tuple[Tuple[int]]:
        """ Get box for draw """
        return (self.x, self.y), (self.x + self.w, self.y + self.h)
    
    def update_coordinates(self, box: List[int]) -> None:
        """ Update coordinates of person """
        self.x = int(box[0])
        self.y = int(box[1])
        self.w = int(abs(box[0] - box[2]))
        self.h = int(abs(box[1] - box[3]))
        self.cx = int(self.x + self.w / 2) # Cast to int because pixel can't be a fractional
        self.cy = int(self.y + self.h / 2) # Cast to int because pixel can't be a fractional
        self.trace.append((self.cx, self.cy))
