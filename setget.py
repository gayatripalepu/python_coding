class Student:
    def __init__(self,rno,name):
        self.__no=rno
        self.__name=name
    @property
    def rno(self):
        return self.__no
    @rno.setter
    def rno(self,rno):
        self.__no=rno
    @rno.deleter
    def rno(self):
        del self.__no
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    @name.deleter
    def name(self):
        del self.__name
        print("from del")

s=Student(0,"")
s.rno=1002
s.name="karthikeya"
print(s.rno,s.name)
print(s.rno,s.name)
del s.name
print(s.rno)
