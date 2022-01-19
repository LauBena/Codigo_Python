from os import system

nombre_1 = input('Escribe tu nombre: ')
system('cls')
edad_1 = int(input(f'{nombre_1} indica que edad tienes: '))
system('cls')

nombre_2 = input('Escribe tu nombre: ')
system('cls')
edad_2 = int(input(f'{nombre_2} Indica que edad tienes: '))
system('cls')

if edad_1 > edad_2:
    print(nombre_1 + ' es mayor que ' + nombre_2)
elif edad_1 < edad_2:
    print(nombre_2 + ' es mayor que ' + nombre_1)
else:
    print('Ambos tienen la misma edad')