import math
'''
Fazer um programa para ler as medidas da base e altura de um retângulo.
Em seguida, mostrar o valor da área, perímetro e diagonal deste retângulo,
com quatro casas decimais.
'''

base = float(input("Base do retangulo: "))
altura = float(input("Altura do retangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt(base * base + altura * altura)

print(f"AREA = {area:.4f}")
print(f"PERIMETRO = {perimetro:.4f}")
print(f"DIAGONAL = {diagonal:.4f}")
