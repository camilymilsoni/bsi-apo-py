'''
Faça um algoritmo que leia 50 valores reais e armazene em um vetor.
Modifique o vetor de modo que os valores das posições ímpares sejam aumentados em 5%, 
e os das posições pares sejam aumentados em 2%. Imprima depois o vetor resultante.
OBS: Para saber se um número é par você pode estar usando o comando %. Ex:  10 % 2, essa linha de comando retorna 
o resto da divisão do número 10 por 2, caso o resto da divisão for igual a zero, o número é par.
'''

cont = 0
vet = [0.0]*50

for cont in range(0,50,1):
    vet[cont] = float(input(f"Informe o número para a posição {cont}: "))

    if(cont % 2 == 0):
        vet[cont] = 1.02 * vet[cont]
    else:
        vet[cont] = 1.05 * vet[cont]

print("Vetor resultante após as modificações: ")

for cont in range(0,50,1):
    print(f"[{vet[cont]:,.2f}]", end= '')