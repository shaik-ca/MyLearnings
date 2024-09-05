#print(list(range(100)))
#Iterating Over a List
# names=["Rabbani","Idreess","Zainab"]

# #Iterating Over a Range of Numbers
# for i in range(100):
#      print(i+1)
# i=1;   
# for name in names:
#      print(f'counter:{i}-{name}')
#      i+=1

# name="RABBANI"
# for char in name:
#     print(char)

#range(start, stop[, step]) 
    ##help(range)
from math import *
# num=eval(input("Enter a number:"))
# for i in range(1,num+1,1):
#     print(f'Squre root of {i} is: {sqrt(i)}')    
# display mutiplication table up to 10 for give number
num=eval(input("Enter a number:"))
limit=eval(input("Enter limit:"))
for i in range(1,limit+1):
    print(f'{num} X {i} = {num*i}')