class A:
    def showA(self):
        print("from a")
class B(A):
    def showB(self):
        print("from b")
class C:
    def showC(self):
        print("from c")
class D(B,C):
    def showD(self):
        print("from d")
d=D()
d.showA()
d.showB()
d.showC()
d.showD()
