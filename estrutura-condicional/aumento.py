'''
Uma empresa vai conceder um aumento percentual de salário aos seus
funcionários dependendo de quanto 20% cada pessoa ganha, conforme
tabela abaixo. Fazer um 15% programa para ler o salário de uma pessoa,
daí mostrar qual o novo salário desta pessoa depois do aumento,
quanto foi o aumento e qual foi a porcentagem de aumento.

Salario atual:
Ate R$ 1000,00 - aumemento de 20%
Acima de R$ 1000.00 ate R$ 3000.000 - aumento de 15%
Acima de R$ 3000.00 ate R$ 8000.000 - aumento de 10
Acima de R$ 8000.00 - aumento de 5%
'''

salario = float(input("Digite o salário do funcionario: R$ "))

if salario <= 1000.00:
    percentual = 20
elif salario <= 3000.00:
    percentual = 15
elif salario <= 8000.00:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Percentual de aumento aplicado: {percentual}%")
print(f"Valor do aumento: R$ {aumento}")
print(f"Novo salário: R$ {novo_salario}")

