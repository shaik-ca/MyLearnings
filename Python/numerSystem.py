#default number system is used in python is decimal.
x=25
print(f'{x}')
print(f'{x:0d}')
print(f'{x:0b}')
print(f'{x:0o}')
print(f'{x:0x}')

#Number alignment
x=2
print(f'{x:_<5}')#right
print(f'{x:0>5}')#lef
print(f'{x:0^5}')#center

print("-----------------------")

print('1,2,3,4')
print('5,6,7,8')
print('9,10,11,12')
print('1,2,13,14')

print(f'{1:>4}{2:>4}{3:>4}{4:>4}')
print(f'{5:>4}{1:>4}{1:>4}{1:>4}')
print(f'{9:>4}{10:>4}{11:>4}{12:>4}')
print(f'{1:>4}{2:>4}{13:>4}{14:>4}')

x=3680
hours=round(x/60)
minutes=(x%60)

print(f'{hours:<4}:{minutes:>4}')

x=3680
hours=round(x/60)
minutes=(x%60)
sec=(minutes%60)

print(f'{hours:<4}:{minutes:>4}:{sec:>4}')
