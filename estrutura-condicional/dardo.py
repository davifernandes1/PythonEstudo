arremeso1 = float(input("Digite a distancia do primeiro arremeso: "))
arremeso2 = float(input("Digite a distancia do segundo arremeso: "))
arremeso3 = float(input("Digite a distancia do terceiro arremeso: "))

if (arremeso1 > arremeso2) and (arremeso1 > arremeso3):
  maior = arremeso1
else:
  if (arremeso2 > arremeso1) and (arremeso2 > arremeso3):
    maior = arremeso2
  else:
    maior = arremeso3

print(maior)
