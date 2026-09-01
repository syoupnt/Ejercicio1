i = 0

while i < 10:
    print(f'Saludo #{i+1} ', end='')
    if i % 2:
        print('es par')
    else:
        print('es impar')

    i += 1