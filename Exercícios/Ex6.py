'''
 Uma empresa revendedora de sucos vende seu produto nos formatos: lata de 350ml,
 garrafa de 600ml e garrafa de 2 litros. Faça um algoritmo que receba a quantidade 
 comprada de cada item por uma determinada pessoa e informe ao final a quantidade
 total de litros de suco que essa pessoa comprou.
 Ex: suponha que a pessoa comprou uma lata de 350ml e uma garrafa de 2 litros, o 
 total comprado foi de 2.35 litros.
'''

lata, gar6, gar2, total = 0, 0, 0, 0.0

lata = int(input("Digite a quantidade comprada de latas de 350ml: "))
gar6 = int(input("Digite a quantidade comprada de garrafas de 600ml: "))
gar2 = int(input("Digite a quantidade comprada de garrafas de 2 litros: "))

lata = lata * 0.35
gar6 = gar6 * 0.6
gar2 = gar2 * 2
total = lata + gar6 + gar2

print(f"O total comprado de litros de suco é {total} litros.")