'''
Fazer um programa para ler três números inteiros.
Em seguida, mostrar qual o menor dentre os três números lidos.
Em caso de empate, mostrar apenas uma vez.
'''

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if (numero1 < numero2) and (numero1 < numero3):
  menor = numero1
elif numero2 < numero3:
   menor = numero2
else:
    menor = numero3

print(menor)

