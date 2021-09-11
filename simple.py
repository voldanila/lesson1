a = 2
b = 0.5
print(a + b)

name = input('Enter your name: ')
name_cap = name.capitalize()
print(f'Hi, {name_cap}!')

v = input('Enter numeric from 1 to 10: ')
c = float(v) + 10
print(c)

name = input('Enter your name: ')
name_c = name.upper()
print(f'Hi, {name_c}! How are you?')

a = float('1')
# b = int('2.5') нельзя преобразовать число с плавающей точкой в целое
b = 'нельзя преобразовать число с плавающей точкой в целое'
c = bool(1)
d = bool('')
e = bool(0)
print(f' {a}, {b}, {c}, {d}, {e}')

