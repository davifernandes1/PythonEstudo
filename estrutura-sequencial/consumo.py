'''
Fazer um programa para ler a distância total (em km) percorrida por um carro,
bem como o total de combustível gasto por este carro ao percorrer tal distância.
Seu programa deve mostrar o consumo médio do carro, com três casas decimais.
'''



distancia = float(input("Distancia percorrida: "))
combustivel = float(input("Combustivel gasto: "))

consumo = distancia / combustivel

print(f"Consumo medio = {consumo:.3f}")
