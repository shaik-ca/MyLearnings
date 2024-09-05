def myFunction(name):
    return f'Hello {name} Welcome to python world...'


myName=input("Enter name:")

print(myFunction(myName))

def myFunctionMultiReturn(x,y):
    return x,y

x,y=myFunctionMultiReturn(20,30)
print(x,y)
print(myFunctionMultiReturn(10,20))