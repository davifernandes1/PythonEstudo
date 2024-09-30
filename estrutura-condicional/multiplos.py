'''
Fazer um programa para ler dois números inteiros, e dizer se um número
é múltiplo números podem ser digitados em qualquer ordem.
'''

x = int(input("Digite um numero inteiro: "))
y = int(input("Digite um numero inteiro: "))

if x % y == 0 or y % x == 0:
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")
