class Number:
    @staticmethod
    def Convert(s):
        if(type(s)==str):
            return int(s)

n=Number.Convert("20")
print(type(n))
print(n)
