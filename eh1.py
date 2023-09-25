a=10
b=20
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("divide error")
print("main")
