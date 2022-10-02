'''
O custo ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor
e dos impostos ao preço de fábrica. Faça um programa que receba o preço de fábrica de um veículo, 
o percentual de lucro do distribuidor e o percentual de impostos. 
Calcule e mostre:
    a) o valor correspondente ao lucro do distribuidor;
    b) o valor correspondente ao imposto;
    c) o preço final do veículo.
'''

precoFab, lucroDist, imp, valorF = 0.0, 0.0, 0.0, 0.0

precoFab = float(input("Informe o preço de fábrica do veículo: R$"))
lucroDist = float(input("Informe o percentual de lucro do distribuidor: "))
imp = float(input("Informe o percentual de impostos: "))

lucroDist = (lucroDist/100) * precoFab
imp = (imp/100) * precoFab 
valorF = precoFab + lucroDist + imp

print(f"O valor correspondente ao lucro do distribuidor é: R${lucroDist}")
print(f"O valor correspondente ao imposto é: R${imp}")
print(f"O preço final do veículo é: R${valorF}")