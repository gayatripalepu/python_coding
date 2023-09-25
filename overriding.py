class Base:
    def show(self):
        print("from base show")
class Derived(Base):
    def show(self):
        super().show()
        print("from derived show")
d=Derived()
d.show()
