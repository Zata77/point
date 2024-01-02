from math import *
class Point:
    def __init__(self,a=0,b=0):
        self.__a = a
        self.__b = b

    def getx(self):
        return self.__a
    
    def gety(self):
        return self.__b
    
    def setx(self,x):
        self.__a = x
        
    
    def sety(self,y):
        self.__b = y

    def deplace(self,dx,dy):
        self.setx(self.getx()+dx)
        self.sety(self.gety()+dy)

    def affiche(self):
        print("x=",self.getx())
        print("y=",self.gety())
    
    def saisire(self):
        print("entrer x et y :")
        self.__x=int(input("x="))
        self.__y=int(input("y="))

    def distance(self,p):
        x1=(self.getx()-p.getx())
        x2=(self.gety()-p.gety())
        dist=sqrt(x1+x2)
        return dist
    
    def milieu(self,p):
       p1 = Point()
       p1.x=(self.getx()+p.getx())/2
       p1.y=(self.gety()+p.gety())/2
       return p1

p = Point(4,8)
p2 = Point(3,5)
p3 = Point(5,2)
p.affiche()
p.deplace(3,7)
p.affiche()
print("la distance px est: ",p.distance(p2))
p3=p.milieu(p2)
print("le milieu de px est: (",p2.getx(),",",p2.gety(),")")



        
        
    
        