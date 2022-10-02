cont = 0
vet = [0]*5

for cont in range(0,5,1):
    vet[cont] = int(input(f"Informe o número para a posição {cont}: "))

for cont in range(0,5,1):
    print(f"[{vet[cont]}]", end= ' ') #comando end= ' ' : para não quebrar a linha após cada número digitado na tela