class Gp:
    def showGp(self):
        print("from gp")
class P(Gp):
    def showP(self):
        print("from p ")
class C(P):
    def showC(self):
        print("from c")
c=C()
c.showGp()
c.showP()
c.showC()
