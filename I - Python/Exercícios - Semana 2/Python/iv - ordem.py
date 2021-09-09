"""
Faça um Programa que leia três números e
mostre-os em ordem decrescente.
"""

num1 = int(input('Insira o número: '))
num2 = int(input('Insira o número: '))
num3 = int(input('Insira o número: '))

if num1 > num2 and num2 > num3:
    print(f'{num1} -> {num2} -> {num3}')
elif num2 > num1 and num1 > num3:
    print(f'{num2} -> {num1} -> {num3}')
elif num3 > num1 and num1 > num2:
    print(f'{num3} -> {num1} -> {num2}')
else:
    print(f'{num3} -> {num2} -> {num1}')