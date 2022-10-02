'''
Amostra de classificação do solo:
Rochosa: se menos ou igual a 10 pontos de água
Firme: se mais do que 10 e menos ou igual a 40 pontos
Pantanosa: se mais do que 40 e menos ou igual a 80 pontos
Quantidade Inválida: se mais do que 80 pontos
'''

qtd = 0

qtd = int(input("Informe a quantidade de pontos de água presente no solo: "))

if(qtd <= 10):
    print(f"O tipo do solo é Rochoso.")
else:
    if((qtd > 10) and (qtd <= 40)):
        print(f"O tipo do solo é Firme.")
    else:
        if((qtd > 40) and (qtd <= 80)):
            print(f"O tipo do solo é Pantanoso.")
        else:
            print(f"Quantidade inválida.")

