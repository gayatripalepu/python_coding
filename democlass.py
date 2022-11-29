class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"name={self.name},age={self.age}"
p1 = person("apple",30)
print(p1)
