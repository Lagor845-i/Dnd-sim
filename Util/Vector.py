from typing import Optional

class Vector():
    def __init__(self,x:float = 0,y:float = 0,z:Optional[float] = None) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        if isinstance(other,Vector):
            self.x += other.x
            self.y += other.y
            if self.z == None:
                if other.z == None:
                    pass
                else:
                    self.z = other.z
            else:
                if other.z == None:
                    pass
                else:
                    self.z += other.z
    
    def __sub__(self, other):
        if isinstance(other,Vector):
            self.x -= other.x
            self.y -= other.y
            if self.z == None:
                if other.z == None:
                    pass
                else:
                    self.z = other.z
            else:
                if other.z == None:
                    pass
                else:
                    self.z -= other.z