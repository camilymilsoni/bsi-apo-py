cont = 0
vet = [""]*5

for cont in range(0,5,1):
    vet[cont] = input(f"Informe o texto para a posição {cont}: ")

for cont in range(0,5,1):
    print(f"[{vet[cont]}]", end= ' ')