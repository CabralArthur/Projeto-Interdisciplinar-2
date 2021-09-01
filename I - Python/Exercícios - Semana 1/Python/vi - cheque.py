""" 
Ler o valor de um cheque e escrever o quanto 
vai ser recolhido de CPMF. Considere que 
imposto recolhe uma taxa de 0,3%. Imprimir 
o valor do imposto.
"""

valor = float(input("Insira aqui o valor do cheque: "))

recolhido = valor * 0.3 / 100

print("O valor recolhido será:", recolhido)