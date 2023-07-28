class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Rect(Shape):
    def area(self):
        return(self.x *self.y)
class Square(Shape):
    def area(self):
        return(self.x*self.x)
r=Rect(10,20)
print(r.area())
s=Square(10,0)
print(s.area())
