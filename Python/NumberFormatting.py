#Option 1:
x=10000000
print(f"{x:,}") #THousand Separator

#Option 2:
x=100_00_000
print(f"{x:,}") #THousand Separator - FOrmatter nohting to do with under scrore in the x

#Dispaly sign of the numer:
x=10.265121
print(f"{x:-}") #THousand Separator - FOrmatter nohting to do with under scrore in the x
print(f"{x:+}") #THousand Separator - FOrmatter nohting to do with under scrore in the x

#rounding up..
print(round(x,2))
print(f'{x:.2f}')

#%..
print(f'{x:.2f}')
print(f'{x:.2%}')#mutilple formatters in one line
print(f'{x:+.2%}')#mutilple formatters in one line
print(f'{x:+,.2%}')#mutilple formatters in one line

print(f'{x:E}')#Exponential value.
print(f'{x:+.2e}')#Exponential value.