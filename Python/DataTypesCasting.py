
# Converting into float
# a=10
# b=float(a)
# print(a,b)
# print(type(a))
# print(type(b))

# # Convert float to int. will loose decimal portion

# a=int(10.9)
# print(a)
# print(type(a))

# # Convert any type to string
# x=str(a)
# print (str(a))
# print(type(x))

x=eval(input("Please enter threee digit number:"))
a=x%10
x=x//10
b=x%10
c=x//10

print(a)
print(b)
print(c)
print(a,"+",b,"+",c,"is :",a+b+c)
# print using fstring

print(f"{a} + {b} + {c} is",a+b+c)
