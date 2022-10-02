'''
Faça um programa que receba uma medida em pés.
Faça as conversões a seguir e mostre os resultados.
    a) polegadas
    b) jardas
    c) milhas
Sabe-se que:
    1 pé = 12 polegadas
    1 jarda = 3 pés
    1 milha = 1760 jardas
'''

pes, pol, jar, mil = 0.0, 0.0, 0.0, 0.0


pes = float(input("Digite a medida em pés: "))

pol = pes * 12
jar = pes / 3
mil = jar / 1760

print(f"O valor de pés em polegadas é: {pol}")
print(f"O valor de pés em jardas é: {jar:,.2f}")
print(f"O valor de pés em milhas é: {mil:,.5f}")