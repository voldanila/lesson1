print('Привет мир!')
print("Привет программист!")
print(2+2)
print(10/3)

name = 'Danila'
print (name)

a = 'Hi'
b = "Hi"
c = a == b
print(c)

a = 3
b = 0
c = a > b
print(c)

a = 'Hi'
b = "World"
c = a + ' ' + b
print(c)

a = 'Hi'
b = "World"
c = f'{a} {b}!'
print(c)

a = 'Hi'
b = "World"
c = f'{a} {b}!'
print(len(c))

a = 'Hi'
b = "World"
c = f'{a} {b}!'
print(c.upper())

a = '   Hi   '
print(a.strip())

a = 'Прив3т т3б3'.replace('3', 'e')
print(a)

a = 'ПриветЫ'.lower()
b = a.replace('ы', '')
c = b.capitalize()
print(c)

a = 'ПриветЫ'.lower().replace('ы', '').capitalize()
print(a)  

a = "learn.python.ru"
print(a.split('.'))

a = "Предложение из нескольких слов"
print(len(a.split()))

a = "Предложение из нескольких слов"
b = a.split()
c = len(b)
print(c)

name = input('Enter your name: ')
print(f'Hi, {name}')

year = input('Write your birthday year: ')
real_age = 2021 - int(year)
print(f'Your age is {real_age}')










