'''
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.
'''

preco = float(input("Digite o preco unitario do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))
valor = float(input("Valor dado em dinheiro pelo cliente: "))

if valor >= preco * quantidade:
  troco = valor - preco * quantidade 
  print(f"TROCO = {troco:.2f}")
else: 
  resto = valor - preco * quantidade
  print(f"FALTOU = {resto:.2f}")


