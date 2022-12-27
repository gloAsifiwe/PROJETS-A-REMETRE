from abc import ABCMeta, abstractclassmethod
from math import * #importer tout ce qu'il ya en math


class forme_geometrique(metaclass= ABCMeta):
    @abstractclassmethod
    def surface(self):
        return
    def perimetre(self):
        return
class rectangle(forme_geometrique):
    def __init__(self,H,L) :
        self.H = H
        self.L = L
    def surface(self):
        return self.H * self.L
    def perimetre(self):
        return (self.L+self.H)*2
    
    
class triangle(forme_geometrique):
    def __init__(self,H,B,T) :
        self.H = H
        self.B = B
        self.T= T
    def surface(self):
        return (self.H * self.B)/2
    def perimetre(self):
        return self.B+self.H+self.T
    
    
class cercle(forme_geometrique):
    def __init__(self,R) :
        self.R = R
    def surface(self):
        return  pi*self.R**2
    def perimetre(self):
        return 2*self.R*pi
    
    
class carre(rectangle):
    def __init__(self,H,L) :
        rectangle.__init__(self,H,L)
    def surface(self):
        return self.H *self.H
    def perimetre(self):
        return self.H *4
    
    
class trianglerectangle(rectangle,triangle):
    def __init__(self,H,L,T,B) :
        rectangle.__init__(self,H,L)
        triangle.__init__(self,H,B,T)
        
    def surface(self):
        return (self.H * self.L)/2
    def perimetre(self):
        return self.L+self.H+self.T
    
    
