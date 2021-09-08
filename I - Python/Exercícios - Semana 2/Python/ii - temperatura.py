temp = float(input('Insira aqui a temperatura: '))

if temp >= 39:
    print('Febre Alta')
elif temp >= 37 and temp > 39:
    print('Febril')
else:
    print('Sem febre')