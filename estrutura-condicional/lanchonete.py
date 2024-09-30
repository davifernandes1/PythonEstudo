'''
Uma lanchonete possui vários produtos. Cada produto possui um código e um preço.
Você deve fazer um programa para ler o código e a quantidade comprada de um produto
(suponha um código válido), e daí informar qual o valor a ser pago, com duas casas
decimais, conforme tabela de produtos abaixo:

Codigo e precos dos produtos:
1 = R$ 5.00
2 = R$ 3.50
3 = R$ 4.80
4 = R$ 8.90
5 = R$ 7.32

'''
codigo = int(input("Digite o Codigo do produto comprado: "))
quantidade = int(input("Digite a quantidade do produto comprado: "))

if codigo == 1:
  preco = 5.00 * quantidade
elif codigo == 2:
  preco = 3.50 * quantidade
elif codigo == 3:
  preco = 4.80 * quantidade
elif codigo == 4:
  preco = 8.90 * quantidade
elif codigo == 5:
  preco = 7.32 * quantidade
  
print(preco)
