class A:
    def __init__(self):
        print("from a")
class B(A):
    def __init__(self):
        A.__init__(self)
        print("from b")
b=B()
