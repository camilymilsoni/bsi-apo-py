'''
Pão caseirinho custa R$0.10 e broinha custa R$1.60.
Tem a meta de guardar 10% do total das vendas em uma conta poupança.
Algoritmo deve ler as quantidades vendidas de cada item e depois fazer os cálculos necessários. 
'''

pao, broa, total, poup = 0, 0, 0.0, 0.0

pao = int(input("Informe a quantidade vendida de pão caseirinho: "))
broa = int(input("Informe a quantidade vendida de broinha: "))

pao = pao * 0.1
broa = broa * 1.6
total = pao + broa
poup = 0.1 * total

print(f"O valor vendido de caseirinhos é: R${pao:,.2f}")
print(f"O valor vendido de broinhas é: R${broa:,.2f}")
print(f"O total geral vendido é: R${total:,.2f}")
print(f"O valor que deverá ser guardado na poupança é: R${poup:,.2f}")