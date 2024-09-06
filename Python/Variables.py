'''LEGB Rule'''

def function1():
    x=10
    print(f'X inside funtion1 :{x}')

def function2():
    x=100
    print(f'X inside funtion2 :{x}')

global x
x=10
function1()
function2()
print(f'X Main funtion1 :{x}')
