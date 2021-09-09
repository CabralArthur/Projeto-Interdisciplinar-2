"""
Faça um Programa que peça para entrar com
um ano (inteiro com 4 dígitos) e determine se
o mesmo é ou não bissexto (divisível por 4).
"""

ano = int(input('Digite o ano: '))

if ano % 2 == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')