
contador, numero, soma, maior, menor = 0, 0, 0, 0, 0
media = 0.0

numero = int(input("Digite um número: "))

for contador in range (0, numero, 1):
    idade = int(input(f"Digite a idade {contador + 1}: "))
    
    if(contador == 0):
        maior = idade
        menor = idade
    else:
        if(idade > maior):
            maior = idade
    
        if(idade < menor):
            menor = idade

    soma = soma + idade

media = soma / numero

print(f"A média é {media:,.2f}, a maior idade é {maior} e a menor idade é {menor}.")
